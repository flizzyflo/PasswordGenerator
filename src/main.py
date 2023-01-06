
from UserInterface.PasswordGenerator import PasswordGeneratorFrame
from Settings.settings import TOOL_TITLE, MIN_LENGTH, MAX_LENGTH
import tkinter as tk
from tkinter import simpledialog

global password_length


def change_pw_length(password_generator: PasswordGeneratorFrame) -> None:
    
    """Grabs the password lenght one decicdes to set and sends the information th the password generator to pass 
    it into the password generation function when button is clicked. Takes care of min and maxlength for the password."""

    global password_length
    
    new_password_length = simpledialog.askinteger("Password length", "Select password length: ", minvalue= MIN_LENGTH, maxvalue= MAX_LENGTH)
    password_generator.generate_button.config(command= lambda: password_generator.present_password(password_length= new_password_length))


if __name__ == "__main__":

    root = tk.Tk()
    generator_frame = PasswordGeneratorFrame(master= root)
    generator_frame.pack()
    root.title(TOOL_TITLE)

    # set up user menu
    user_menu = tk.Menu(master= root)
    root.config(menu= user_menu)
    file_menu = tk.Menu(user_menu)

    user_menu.add_cascade(label="File", menu= file_menu)

    file_menu.add_command(label= "Change password length", command= lambda: change_pw_length(password_generator= generator_frame))
    file_menu.add_separator()
    file_menu.add_command(label= "Quit Application", command= lambda: quit())
    
    root.mainloop()
