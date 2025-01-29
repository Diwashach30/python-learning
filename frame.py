## frame using tkinter or GUI

from tkinter import *

root = Tk()
root.geometry("600x600")

frame1 = Frame(root, bg="grey", borderwidth=6 ,relief=SUNKEN) 
frame1.pack(side=LEFT , fill="y")

l=Label(frame1, text="DeepSeek - V3", bg="grey", fg="white", font=("Arial", 12, "bold"))
l.pack(pady=142)

frame2 = Frame(root, bg="grey", borderwidth=8 ,relief=SUNKEN)
frame2.pack(side=TOP , fill="x")

l=Label(frame2, text="WHAT'S YOUR QUESTION ?", bg="grey", fg="white", font=("Arial", 12, "bold"))
l.pack()



root.mainloop()