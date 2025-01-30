## entry and grid using GUI

from tkinter import *

root = Tk()
root.geometry("655x455")

a = Label(root, text="Username : ")
a.grid(column=0, row=0)

b = Entry(root)
b.grid(column=1, row=0)

c = Label(root, text="Password : ")
c.grid(column=0, row=1)

d = Entry(root)
d.grid(column=1, row=1)

button1 = Button(root, text="Login")
button1.grid(column=1, row=2)



root.mainloop()