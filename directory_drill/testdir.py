# directory drill
#
# Python Course Page 122


from tkinter import filedialog
from tkinter import *
import tkinter as tk
from tkinter import messagebox


def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)




# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(500,100) #(Height, Width)
        self.master.maxsize(1000,300)
        self.master.title("The Tkinter Directory Drill")
        self.master.configure(bg="#F0F0F0")
        # This protocol method is a tkinter built-in method to catch if 
        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: ask_quit(self))
        arg = self.master

        # call method
        load_gui(self,folder_path)


def load_gui(self,folder_path):
    # 'Click browse' label
    self.lbl_info = tk.Label(self.master,text='Click Browse to open directory:')
    self.lbl_info.grid(row=0,column=0,rowspan=4,padx=(27,0), pady=(10,0),sticky=N+W)
    # Browse button
    button2 = Button(text="Browse", command=browse_button)
    button2.grid(row=4, column=0,padx=(30,0),pady=(5,0), sticky=W)
    # Directory path label
    lbl1 = Label(master=root,textvariable=folder_path,borderwidth=2, relief="sunken", bg="white")
    lbl1.grid(row=8, column=0,rowspan=7,columnspan=3,padx=(30,0),pady=(5,0),sticky=N+E+S+W)
    
    

    
# catch if the user's clicks on the windows upper-right 'X' to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()






if __name__ == "__main__":
    root = tk.Tk()
    folder_path = StringVar()
    App = ParentWindow(root)
    
    root.mainloop()
    root = Tk()
    

    
