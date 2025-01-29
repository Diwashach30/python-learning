## frame using tkinter or GUI

from tkinter import *

root = Tk()
root.geometry("600x600")

def love():
    print("hello darling")
    
def hate():
    print("hate me too")

frame1 = Frame(root, bg="grey", borderwidth=6 ,relief=SUNKEN) 
frame1.pack(side=LEFT , fill="y")

button1 = Button(frame1, text="HOME", bg="grey", fg="white", font=("Arial", 12, "bold") , command= love)
button1.pack(pady=5)

button2 = Button(frame1, text="ABOUT US", bg="grey", fg="white", font=("Arial", 12, "bold") , command= hate)
button2.pack(pady=5)

button3 = Button(frame1, text="CONTACT", bg="grey", fg="white", font=("Arial", 12, "bold"), command= love)
button3.pack(pady=5)

button4 = Button(frame1, text="LOGOUT", bg="grey", fg="white", font=("Arial", 12, "bold"), command= hate)
button4.pack(pady=5)



frame2 = Frame(root, bg="grey", borderwidth=8 ,relief=SUNKEN)
frame2.pack(side=TOP , fill="x")


l=Label(frame2, text="WHAT'S YOUR QUESTION ?", bg="grey", fg="white", font=("Arial", 12, "bold"))
l.pack()



root.mainloop()