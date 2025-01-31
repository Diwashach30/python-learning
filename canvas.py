## canvas in GUI


import tkinter as tk

root = tk.Tk()
root.geometry("600x600")
root.title("Canvas Line Example")

# Create a Canvas widget
canvas = tk.Canvas(root, width=400, height=300, bg="green")


##Basic straight line (x0, y0, x1, y1)
canvas.create_line(0, 0, 400, 300,  fill="white")
canvas.create_line(0, 300, 400, 0,  fill="white")

canvas.create_rectangle(50,200 , 200, 50 , fill="white" , outline="black" , )
canvas.create_polygon(200,0 , 400, 300 , 0 , 300 , fill="yellow" , outline="black" )

canvas.create_oval( 0, 0, 400, 300, style= "arc" , fill="white", outline="black")

canvas.create_arc( 0 ,0 , 400, 300 , start = 270 ,extent= 180 , fill="white" , outline="black" )
canvas.pack()





root.mainloop()