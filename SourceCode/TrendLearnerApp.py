#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *
from ttk import Frame, Button, Label, Style


class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        self.initUI()
        
        
    def initUI(self):
      
        self.parent.title("TrendLearnerApp")
        self.pack(fill=BOTH, expand=True)

        
        ###InserindoMenu
        self.menubar = Menu(self)

        menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Project",menu=menu)
        menu.add_command(label="New Project")
        menu.add_command(label="Open Project")
        menu.add_command(label="Save")
        menu.add_separator()
        menu.add_command(label="Exit", command=self.master.destroy)

        menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Edit",menu=menu)
        menu.add_command(label="Cut")
        menu.add_command(label="Copy")
        menu.add_command(label="Paste")

        menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Help",menu=menu)
        menu.add_command(label="About TrendLearnerApp")

        try:
            self.master.config(menu=self.menubar)
        except AttributeError:
            self.master.tk.call(master, "config", "-menu", self.menubar)
        ##FimInserindoMenu



        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)
        
        #lbl = Label(self, text="Windows")
        #lbl.grid(sticky=W, pady=4, padx=5)
        
        #area = Text(self)
        #area.grid(row=1, column=1, columnspan=3, rowspan=4, 
        #    padx=5, sticky=E+W+S+N)
        
        abtn = Button(self, text="Activate")
        abtn.grid(row=1, column=0)

        cbtn = Button(self, text="Close")
        cbtn.grid(row=2, column=0, pady=4)
        
        hbtn = Button(self, text="Help")
        hbtn.grid(row=5, column=3, padx=5)

        obtn = Button(self, text="OK")
        obtn.grid(row=5, column=0)        
              

def main():
  
    root = Tk()
    window_width = root.winfo_screenwidth()
    window_height = root.winfo_screenheight()
    root.geometry("%dx%d"%(window_width,window_height))
    #root.geometry("350x300+300+300")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  
