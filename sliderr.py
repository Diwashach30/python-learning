#Create a slider in python using tkinter which consits of message dialog box also

from tkinter import *
from tkinter import messagebox as tmsg

root = Tk()
root.geometry("600x600")
root.title("Slider")

def getdollar():
    print(f"We have credited {slider.get()} dollars to your account" )
    tmsg.showinfo("Dollars", f"We have credited {slider.get()} dollars to your account" )


Label(root, text="How Many Dollars do you want: ").pack()




slider = Scale(root, from_=0, to=100, orient=HORIZONTAL , tickinterval=50)
slider.pack()

Button(root, text="Submit", command=getdollar).pack(
    
)


root.mainloop()