# drill_func.py
#
# Python Course page 121



import os
from tkinter import *
import tkinter as tk
import sqlite3

from tkinter import messagebox


# Be sure to import our other modules 
# so we can have access to them
import drill_main
import drill_gui


# catch if the user's clicks on the windows upper-right 'X' to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
            # Releases user's memory
        os._exit(0)
