## create a GUI window which takes as input width and height and upon clicking apply, it should be able
## to resize the window to that width and height

from tkinter import *   

root = Tk()
root.geometry("600x600")
root.title("Window Resizer")

def getvals():
    print(width.get())
    print(height.get())

width = IntVar()
height = IntVar()

Label(root, text="Width").grid(row=0, column=0)
Label(root, text="Height").grid(row=1, column=0)

Entry(root, textvariable=width).grid(row=0, column=1)
Entry(root, textvariable=height).grid(row=1, column=1)

Button(root, text="Apply", command=lambda: root.geometry(f"{width.get()}x{height.get()}")).grid(row=2, column=1)

root.mainloop()