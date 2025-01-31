## create a listbox from tkinter as GUI

from tkinter import *
 
def add():
    global i
    listbox.insert(ACTIVE, f"{i}")
    i+=1
  
    
root = Tk()
root.geometry("600x600")
root.title("Listbox")

i = 1

listbox = Listbox(root)
listbox.pack()
listbox.insert(END, "Python")



Button(root, text="Submit", command= add).pack()


root.mainloop()