## exercise to make newspaper from GUI

from tkinter import *
from PIL import Image, ImageTk

base = Tk()
base.title("Diwash Newspaper")
base.geometry("1180x644")

label = Label(base, text="Diwash Newspaper", bg="grey", font="Arial 19 bold italic")
label.pack()

f1 = Frame(base, bg="lightblue", borderwidth="3", relief=SUNKEN, highlightbackground="black", highlightthickness=1.5)
f1.pack(fill=X, anchor='nw')

p1 = Image.open("2.png")
P1 = ImageTk.PhotoImage(p1)

l1 = Label(f1, image=P1, width=130, height=130)
l1.pack(side=LEFT)
l12 = Label(f1, text='''India won the series by 2-1 against england ''', bg="lightblue",)
l12.pack()

f2 = Frame(base, bg="lightblue", borderwidth="3", relief=SUNKEN, highlightbackground="black", highlightthickness=1.5)
f2.pack(fill=X, anchor='nw')

p2 = Image.open("2.png")
P2 = ImageTk.PhotoImage(p2)

l2 = Label(f2, image=P2, width=130, height=130)
l2.pack(side=LEFT)
l22 = Label(f2, text='''India won the series by 2-1 against england ''', bg="lightblue",)
l22.pack()



base.mainloop()