#creating a pokeman ball using canvas in GUI

from tkinter import *
import tkinter as tk

root = tk.Tk()
root.geometry("600x600")
root.title("Pokeman Ball")

canvas = Canvas(root, width=500, height= 500)

canvas.create_arc( 0 ,0 , 500, 500 , fill = "red", extent= 180 , outline="black", width=8)
canvas.create_arc( 0 ,0 , 500, 500 , fill = "white", extent= 180 , start = 180 , outline="black", width=8)

canvas.create_oval( 190, 190, 310, 310,  fill="white", outline="black" , width=8)
canvas.create_oval( 210, 210, 290, 290,  fill="white", outline= "purple" , width=1)

canvas.pack()
 



root.mainloop()