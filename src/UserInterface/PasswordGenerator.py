import tkinter as tk
import sys
from PasswordGenerator.password_generator import generate_password
from Settings.settings import FONT_SETTINGS

global password_length
password_length = 12

class PasswordGenerator(tk.Frame):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.generate_button = tk.Button(master= self, 
                                         text="Generate password", 
                                         command= lambda: self.present_password(password_length= password_length))
        self.generate_button.pack(fill= tk.X, expand= True)

        self.copy_password_button = tk.Button(master=self, 
                                              text= "Copy password", 
                                              command= lambda: self.copy_password())
        self.copy_password_button.pack(fill= tk.X, expand= True)

        self.quit_button= tk.Button(master= self, 
                                    text= "Quit", 
                                    command= lambda: quit())
        self.quit_button.pack(fill= tk.X, expand= True)

        self.password_widget = tk.Entry(master= self, justify= "center", state= tk.DISABLED)
        self.password_widget.pack(fill= tk.X, expand= True)
  
        self.orig_color = self.copy_password_button.cget("background")


    def present_password(self, password_length: int) -> None:

        password = generate_password(password_length= password_length)
        self.password_widget.config(state= tk.NORMAL)
        self.password_widget.delete(0, tk.END)
        self.password_widget.insert(0, password)

        if self.is_macos():
            self.password_widget.config(bg= self.orig_color)
            self.copy_password_button.configure(text= "Copy password", 
                                                state= tk.NORMAL)

        else:
            self.copy_password_button.configure(text= "Copy password", 
                                                state= tk.NORMAL, 
                                                bg= self.orig_color, 
                                                fg= "black",
                                                justify= "center")


    def copy_password(self) -> None:
        password = self.password_widget.get().rstrip()
        self.clipboard_clear()
        self.clipboard_append(password)

        # case macos; buttons can not be colorized. entry background is colorized instead
        if self.is_macos():
            self.password_widget.config(bg= "green", fg= "black")
            self.copy_password_button.configure(text="Password copied to clipboard", 
                                                state= tk.DISABLED)
        
        # other os
        else:
            self.copy_password_button.configure(text="Password copied to clipboard", 
                                                state= tk.DISABLED, 
                                                fg= "black", 
                                                bg= "green")

    def is_macos(self) -> bool:
        return sys.platform == "darwin"
