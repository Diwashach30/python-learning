##create a form using GUI for dance class

from tkinter import*

def getvals():
    print(f"The student who are willing to dance are :  {name_entry.get()} , {age_entry.get()} , {gender_entry.get()}")

root = Tk()
root.geometry("600x600")
root.title("Dance Class")

name = Label(root , text = "Enter Your Name")
name.grid(row = 0 , column = 0)

age = Label(root , text = "Enter Your Age")
age.grid(row = 1 , column = 0)

gender = Label(root , text = "Enter Your Gender")
gender.grid(row = 2 , column = 0)

name_entry = Entry(root , width = 30)
age_entry = Entry(root, width= 30)
gender_entry = Entry(root, width= 30)

name_entry.grid(row = 0 , column = 1)
age_entry.grid(row = 1 , column = 1)
gender_entry.grid(row = 2 , column = 1)


Button(root , text = "Submit" , command= getvals ).grid(row = 3 , column = 1)



root.mainloop()