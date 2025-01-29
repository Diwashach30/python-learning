from tkinter import *
from PIL import Image, ImageTk

base = Tk()
base.title("Yuniek's Newspaper")
base.geometry("1180x644")
base.minsize(width=300, height=300)

# Header for newspapaer
Header = Frame(base, bg="grey", borderwidth=5, relief=SUNKEN)
Header.pack(side=TOP, fill=X)
t = Label(Header, text="Diwash Newspaper", bg="grey", font="Arial 19 bold italic")
t.pack()

# News 1
f1 = Frame(base, bg="lightblue", borderwidth="3", relief=SUNKEN, highlightbackground="black", highlightthickness=1.5)
f1.pack(fill=X, anchor='nw')

p1 = Image.open("2.png")
P1 = ImageTk.PhotoImage(p1)

l1 = Label(f1, image=P1, width=130, height=130)
l1.pack(side=LEFT)
l12 = Label(f1, text='''India won the series by 2-1 against england ''', bg="lightblue",)
l12.pack()

# News 2
f2 = Frame(base, bg="lightblue", borderwidth="3", relief=SUNKEN, highlightbackground="black", highlightthickness=1.5)
f2.pack(fill=X, anchor='nw')

p2 = Image.open("cricc.png")
P2 = ImageTk.PhotoImage(p2)

l2 = Label(f2, image=P2, width=130, height=130)
l2.pack(side=LEFT)
l22 = Label(f2, text='''Gautam Gambhir is appointed as new coach of indian crickrt in all three format''', bg="lightblue",)
l22.pack()

# News 3
f3 = Frame(base, bg="lightblue", borderwidth="3", relief=SUNKEN, highlightbackground="black", highlightthickness=1.5)
f3.pack(fill=X, anchor='nw')

p3 = Image.open("2.png")
P3 = ImageTk.PhotoImage(p3)

l3 = Label(f3, image=P3, width=130, height=130)
l3.pack(side=LEFT)
l32 = Label(f3, text='''Nepal is playing against big nations in upcoming future.''', bg="lightblue",)
l32.pack()

# News 4
f4 = Frame(base, bg="lightblue", borderwidth="3", relief=SUNKEN, highlightbackground="black", highlightthickness=1.5)
f4.pack(fill=X, anchor='nw')

p4 = Image.open("cricc.png")
P4 = ImageTk.PhotoImage(p4)

l4 = Label(f4, image=P4, width=130, height=130)
l4.pack(side=LEFT)
l42 = Label(f4, text='''Dipendra Singh Airee is set to become new captain of nepali cricket side''', bg="lightblue",)
l42.pack()

base.mainloop()