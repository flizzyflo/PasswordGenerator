import tkinter as tk
import sys
from src.password_generator.password_generator import generate_password


class PasswordGeneratorFrame(tk.Frame):

    def __init__(self, password_length: int, **kwargs) -> None:
        super().__init__(**kwargs)
        self.password_length: int = password_length
        self.generate_button = tk.Button(master=self,
                                         text="Generate password", 
                                         command=lambda: self.present_password(password_length=self.password_length))
        self.generate_button.pack(fill=tk.X,
                                  expand=True)

        self.copy_password_button = tk.Button(master=self, 
                                              text="Copy password",
                                              command=lambda: self.update_gui_copy_password())
        self.copy_password_button.pack(fill=tk.X,
                                       expand=True)

        self.quit_button= tk.Button(master=self,
                                    text="Quit",
                                    command=lambda: quit())
        self.quit_button.pack(fill=tk.X,
                              expand=True)

        self.password_widget = tk.Entry(master=self,
                                        justify="center",
                                        state=tk.DISABLED)
        self.password_widget.pack(fill=tk.X,
                                  expand=True)
  
        self.orig_color = self.copy_password_button.cget("background")

    def present_password(self, password_length: int) -> None:

        """Presents the password within the GUI to the user."""

        password = generate_password(password_length= password_length)
        self.password_widget.config(state= tk.NORMAL)
        self.password_widget.delete(0, tk.END)
        self.password_widget.insert(0, password)

        if self.is_macos():
            self.password_widget.config(bg=self.orig_color)
            self.copy_password_button.configure(text="Copy password",
                                                state=tk.NORMAL)

        else:
            self.copy_password_button.configure(text="Copy password",
                                                state=tk.NORMAL,
                                                bg=self.orig_color,
                                                fg="black",
                                                justify="center")

    def update_gui_copy_password(self) -> None:

        """Updates the gui to signalize the succesful copying of the password to the user. Copies the password to the
        clipboard and one can use the OS-specific hotkey combination to paste the password anywhere."""

        password = self.password_widget.get().rstrip()
        self.clipboard_clear()
        self.clipboard_append(password)

        # case macos; buttons can not be colorized. entry background is colorized instead
        if self.is_macos():
            self.password_widget.config(bg="green",
                                        fg="black")
            self.copy_password_button.configure(text="Password copied to clipboard", 
                                                state=tk.DISABLED)
        
        # other os
        else:
            self.copy_password_button.configure(text="Password copied to clipboard", 
                                                state=tk.DISABLED,
                                                fg="black",
                                                bg="green")

    def is_macos(self) -> bool:

        """Checks whether the current operating system is a macOS system or anything else."""

        return sys.platform == "darwin"
