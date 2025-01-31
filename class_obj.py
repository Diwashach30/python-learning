## using class and objects in python using GUI

from tkinter import *

class GUI (Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x500")
        self.title("Class and Objects")
        
    def status(self):
        self.var = StringVar()
        self.var.set("Welcome to Status Bar")
        self.statusbar = Label(self, textvar=self.var, bd=1, relief=SUNKEN , anchor="w")
        self.statusbar.pack(side=BOTTOM, fill=X)
        
    def click(self):    
        print("Clicked") 
    def button(self , inptext):
        self.button = Button(text=inptext, command=self.click)
        self.button.pack()
        
if __name__ == "__main__":
    root = GUI()
    
    root.status()
    root.button("Click Here")
    root.mainloop()