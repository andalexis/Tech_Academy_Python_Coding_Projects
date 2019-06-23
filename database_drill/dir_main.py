# dir_main.py
#
# Python course page 123


from tkinter import filedialog
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import os

import dir_func
import sqlite3
import shutil


qualifying = []


# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)


        self.folder_path1 = StringVar()
        self.folder_path2 = StringVar()
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
        create_db()

    # move function that use move() method from the Shutil
    # module to cut all qualifying files
    # and paste them within the destination directory
    def move(self):
        # Source Path
        src = self.folder_path1.get()
        # Destination Path
        des = self.folder_path2.get()
        print("src = " + src)
        print("des = " + des)
        dir_list = os.listdir(src)
        # move qualifying files
        for file in dir_list:
            if file.endswith(".txt"):
                absolute = (os.path.join(src,file))
                shutil.move(absolute,des)


    # function for first selected directory
    def browse_button_1(self):
        # Allow user to select a directory and store it in global var
        # called folder_path
        global folder_path1
        filename = filedialog.askdirectory()
        self.folder_path1.set(filename)
        print("filename" + filename)
        iterate(filename)
        
        
    # function for second selected directory
    def browse_button_2(self):
        # Allow user to select a directory and store it in global var
        # called folder_path
        global folder_path2
        filename2 = filedialog.askdirectory()
        self.folder_path2.set(filename2)
        print("filename2" + filename2)




def load_gui(self,folder_path1,folder_path2):
    # First Select 
    # 'Click browse' label
    self.lbl_info = tk.Label(self.master,text='Click Browse to open directory:')
    self.lbl_info.grid(row=0,column=0,rowspan=4,padx=(27,0), pady=(10,0),sticky=N+W)
    # Browse button
    button2 = Button(text="Browse", command=self.browse_button_1)
    button2.grid(row=0, column=4,padx=(30,0),pady=(10,0), sticky=W)
    # Directory path label
    lbl1 = Label(master=root,textvariable=self.folder_path1,borderwidth=2, relief="sunken", bg="white")
    lbl1.grid(row=8, column=0,rowspan=7,columnspan=3,padx=(30,0),pady=(10,0),sticky=N+E+S+W)

    # Second Select
    # 'Click browse' label
    self.lbl_info = tk.Label(self.master,text='Click Browse to open another directory:')
    self.lbl_info.grid(row=20,column=0,rowspan=4,padx=(27,0), pady=(10,0),sticky=N+W)
    # Browse button
    button2 = Button(text="Browse", command=self.browse_button_2)
    button2.grid(row=20, column=4,padx=(30,0),pady=(10,0), sticky=W)
    # Directory path label
    lbl1 = Label(master=root,textvariable=self.folder_path2,borderwidth=2, relief="sunken", bg="white")
    lbl1.grid(row=22, column=0,rowspan=7,columnspan=3,padx=(30,0),pady=(10,0),sticky=N+E+S+W)

    # Move Prompt label
    self.lbl_info = tk.Label(self.master,text='Move all files ending in .txt to selected destination directory:')
    self.lbl_info.grid(row=30,column=0,rowspan=4,padx=(27,0), pady=(10,0),sticky=N+W)
    
    # Move Prompt button
    button2 = Button(text="Move All!", command=self.move)
    button2.grid(row=40, column=0,padx=(30,0),pady=(10,0), sticky=W)
    

    
#Button functions
# function for first selected directory
def browse_button_1(self):
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path1
    filename = filedialog.askdirectory()
    self.folder_path1.set(filename)
    print("filename" + filename)
    #### print commands to see what is happening
    iterate(filename)
    
    
# function for second selected directory
def browse_button_2(self):
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path2
    filename2 = filedialog.askdirectory()
    self.folder_path2.set(filename2)
    print("filename2" + filename2)
    ##iterate(filename,filename2)
    
    

# Function to iterate through selected directory
# and pull out the files ending in .txt
def iterate(filename):
    path = filename
    #qualifying = []
    dir_list = os.listdir(path)
    print("Files in '", path, "' :")
    #print the list
    print(dir_list)
    print("\nThese are all the files ending in '.txt' in this directory: \n")
    for file in dir_list:
        if file.endswith(".txt"):
            print(file)
            qualifying.append(file)
            absolutepath(file,path)
    print(qualifying)
    


# functon that creates the file's absolute path
def absolutepath(file,path):
    print("The absolute file path for this file is: \n")
    absolute = (os.path.join(path,file))
    print(absolute)
    mtime(path,file,absolute)

# function that retieves modified time stamp
def mtime(path,file,absolute):
    mtime = os.path.getmtime(absolute)
    print("The last modification of this path:")
    print(mtime)
    print("\n")
    insertion(file,mtime)


#==========================================
# Sql portion of python drill
#
# Creates database and records the qualifying file
# and coresponding modified time-stamp



def create_db():
    conn = sqlite3.connect('db_timestamp.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_data( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_filename TEXT, \
            col_mtime TEXT \
            );")
        # commit() to save changes & close the database connection
        conn.commit()
    conn.close()


def insertion(file,mtime):
    conn = sqlite3.connect('db_timestamp.db')
    with conn:
        conn.execute("INSERT INTO tbl_data(col_filename, col_mtime) VALUES(?,?)", \
                    (file, mtime))
        conn.commit()
    conn.close()
    
    
    



if __name__ == "__main__":
    root = tk.Tk()
    conn = sqlite3.connect('db_timestamp.db')
    folder_path1 = StringVar()
    folder_path2 = StringVar()
    App = ParentWindow(root)
    
    root.mainloop()
