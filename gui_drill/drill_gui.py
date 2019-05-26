# drill_gui.py
#
# Python Course page 121


from tkinter import *
import tkinter as tk

# Import other modules for access
import drill_main
import drill_func



def load_gui(self):
    """
        Define the default tkinter wdigets and their initial
        configuration and place them using the grid geometry.
        (I prefer to use grid as it offers the best control
        for pacing the widgets, but it is a little confusing at
        first, but that is what this demo is here for...
    """
   
    self.txt_entry1 = tk.Entry(self.master,width=50,text='')
    self.txt_entry1.grid(row=1,column=0,rowspan=1,columnspan=3,padx=(170,40),pady=(35,0),sticky=S+W)
    self.txt_entry2 = tk.Entry(self.master,width=50,text='')
    self.txt_entry2.grid(row=2,column=0,rowspan=1,columnspan=3,padx=(170,40),pady=(20,10),sticky=S+W)
    
    self.btn_browse1 = tk.Button(self.master,width=12,height=1,text='Browse')
    self.btn_browse1.grid(row=1,column=0,rowspan=1,columnspan=2,padx=(15,40),pady=(35,0),sticky=S+W)
    self.btn_browse2 = tk.Button(self.master,width=12,height=1,text='Browse')
    self.btn_browse2.grid(row=2,column=0,rowspan=1,columnspan=2,padx=(15,40),pady=(20,10),sticky=S+W)
    self.btn_check = tk.Button(self.master,width=12,height=2,text='Check for files...')
    self.btn_check.grid(row=3,column=0,rowspan=1,columnspan=2,padx=(15,40),pady=(5,0),sticky=S+W)
    self.btn_close = tk.Button(self.master,width=12,height=2,text='Close Program',command=lambda: drill_func.ask_quit(self))
    self.btn_close.grid(row=3,column=2,rowspan=1,columnspan=2,padx=(0,40),pady=(0,0),sticky=S+E)
