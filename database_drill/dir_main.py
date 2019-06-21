# dir_main.py
#
# Python course page 123


from tkinter import filedialog
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import os

import dir_func





# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(500,300) #(Height, Width)
        self.master.maxsize(1000,300)
        self.master.title("The Tkinter Directory Drill")
        self.master.configure(bg="#F0F0F0")
        # This protocol method is a tkinter built-in method to catch if 
        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: dir_func.ask_quit(self))
        arg = self.master

        # call method
        load_gui(self,folder_path1,folder_path2)


def load_gui(self,folder_path1,folder_path2):
    # First Select 
    # 'Click browse' label
    self.lbl_info = tk.Label(self.master,text='Click Browse to open directory:')
    self.lbl_info.grid(row=0,column=0,rowspan=4,padx=(27,0), pady=(10,0),sticky=N+W)
    # Browse button
    button2 = Button(text="Browse", command=browse_button_1)
    button2.grid(row=0, column=4,padx=(30,0),pady=(10,0), sticky=W)
    # Directory path label
    lbl1 = Label(master=root,textvariable=folder_path1,borderwidth=2, relief="sunken", bg="white")
    lbl1.grid(row=8, column=0,rowspan=7,columnspan=3,padx=(30,0),pady=(10,0),sticky=N+E+S+W)

    # Second Select
    # 'Click browse' label
    self.lbl_info = tk.Label(self.master,text='Click Browse to open another directory:')
    self.lbl_info.grid(row=20,column=0,rowspan=4,padx=(27,0), pady=(10,0),sticky=N+W)
    # Browse button
    button2 = Button(text="Browse", command=browse_button_2)
    button2.grid(row=20, column=4,padx=(30,0),pady=(10,0), sticky=W)
    # Directory path label
    lbl1 = Label(master=root,textvariable=folder_path2,borderwidth=2, relief="sunken", bg="white")
    lbl1.grid(row=22, column=0,rowspan=7,columnspan=3,padx=(30,0),pady=(10,0),sticky=N+E+S+W)

    # Move Prompt
    self.lbl_info = tk.Label(self.master,text='Move all files ending in .txt to selected destination directory:')
    self.lbl_info.grid(row=30,column=0,rowspan=4,padx=(27,0), pady=(10,0),sticky=N+W)
    
    # Move button
    button2 = Button(text="Move All!", command=browse_button_2)
    button2.grid(row=40, column=0,padx=(30,0),pady=(10,0), sticky=W)
    

    
    

# function for first selected directory
def browse_button_1():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path1
    filename = filedialog.askdirectory()
    folder_path1.set(filename)
    print(filename)
    iterate(filename) #new addition
    
# function for second selected directory
def browse_button_2():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path2
    filename = filedialog.askdirectory()
    folder_path2.set(filename)
    print(filename)


# function to iterate through selected directory
# and pull out the files ending in .txt
def iterate(filename):
    path = filename
    dir_list = os.listdir(path)
    print("Files in '", path, "' :")
    #print the list
    print(dir_list)
    print("\nThese are all the files ending in '.txt' in this directory: \n")
    for file in dir_list:
        if file.endswith(".txt"):
            print(file)
            absolutepath(file,path)

def absolutepath(file,path):
    print("The absolute file path for this file is: \n")
    absolute = (os.path.join(path, file) + "\n")
    print(absolute)
    mtime(path,file,absolute)

def mtime(path,file,absolute):
    mtime = os.path.getmtime(file)
    print("The last modification of this path: \n")
    print(mtime)
    














if __name__ == "__main__":
    root = tk.Tk()
    folder_path1 = StringVar()
    folder_path2 = StringVar()
    App = ParentWindow(root)
    
    root.mainloop()
