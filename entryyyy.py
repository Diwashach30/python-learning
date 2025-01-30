# basically i am learning to use entry and label in GUI


from tkinter import *

def getvals():
    print(f"The Value of username is {username.get()}")
    print(f"The Value of password is  {password.get()}")


root = Tk()

root.geometry("600x600")

user = Label(root , text = "username")
password = Label(root , text = "password")
user.grid()
password.grid(row = 1)

username = Entry(root )
password = Entry(root)

username.grid(row = 0 , column=1)
password.grid(row = 1 , column=1)

Button(root , text = "Login" , command= getvals()).grid(row = 2 , column = 1)




root.mainloop()
