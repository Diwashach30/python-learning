## creating a status bar using GUI

from tkinter import *
from tkinter import messagebox as tmsg

root = Tk()
root.geometry("500x500")
root.title("Status Bar")

def upload():
    statusvar.set("Hello")
    status.update()
    import time
    time.sleep(2)
    tmsg.showinfo("Success", "File Uploaded Successfully")


statusvar = StringVar()
statusvar.set("Welcome to Status Bar")
status = Label(root, textvariable=statusvar, bd=1, relief=SUNKEN)
status.pack(side=BOTTOM, fill=X)

Button(root, text="Click Here", command=upload).pack()




root.mainloop()