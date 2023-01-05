
from UserInterface.PasswordGenerator import PasswordGenerator
from Settings.settings import TOOL_TITLE, MIN_LENGTH, MAX_LENGTH
import tkinter as tk
from tkinter import simpledialog

global password_length


def change_pw_length(password_generator: PasswordGenerator) -> None:
    
    global password_length
    
    new_length = simpledialog.askinteger("Password length", "Select password length: ", minvalue= MIN_LENGTH, maxvalue= MAX_LENGTH)
    password_generator.generate_button.config(command= lambda: password_generator.present_password(password_length= new_length))


if __name__ == "__main__":

    root = tk.Tk()
    p = PasswordGenerator(master= root)
    p.pack()
    root.title(TOOL_TITLE)
    user_menu = tk.Menu(master= root)
    root.config(menu= user_menu)
    file_menu = tk.Menu(user_menu)

    user_menu.add_cascade(label="File", menu= file_menu)

    file_menu.add_command(label= "Set password length", command= lambda: change_pw_length(password_generator= p))
    file_menu.add_command(label= "Quit", command= lambda: quit())
    root.mainloop()
