## creating radiobuttons using GUI

from tkinter import *

from tkinter import messagebox as tmsg

root = Tk()
root.geometry("500x500")
root.title("Radio Buttons")

def order():
    if var.get() == 1:
        tmsg.showinfo("Order" , "You have ordered a tea")
    elif var.get() == 2:
        tmsg.showinfo("Order" , "You have ordered a coffee")
    elif var.get() == 3:
        tmsg.showinfo("Order" , "You have ordered a hot chocolate"),

var = IntVar()
var.set("1")

Label (root , text = "What would you like to have sir ?" , justify= LEFT , padx= 20 , font = ("Arial", 12, "bold")).pack()

radio = Radiobutton(root, text = "Tea" , variable = var , value = 1 , font = ("Arial", 6, "bold")).pack(anchor="w")
radio = Radiobutton(root, text = "Coffee" , variable = var , value = 2 , font = ("Arial", 6, "bold")).pack(anchor="w")
radio = Radiobutton(root, text = "Hot Chocolate" , variable = var , value = 3 , font = ("Arial", 6, "bold")).pack(anchor="w")

Button(root , text = "Order" , command = order).pack()


root.mainloop()