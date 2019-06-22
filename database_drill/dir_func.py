# dir_main.py
#
# Python course page 123


from tkinter import filedialog
from tkinter import *
import tkinter as tk
from tkinter import messagebox

import dir_main

# folder_path not defined. variable import error?

    #def browse_button():
        # Allow user to select a directory and store it in global var
        # called folder_path
        #global folder_path
        #filename = filedialog.askdirectory()
        #folder_path.set(filename)


def ask_quit(self):
    # catch if the user's clicks on the windows upper-right 'X' to ensure they want to close
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()


#=====================================================================




if __name__ == "__main__":
    folder_path = StringVar()
    pass
