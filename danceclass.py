from tkinter import *

root = Tk()

def getvals():
    print(f"{namevalue.get(), agevalue.get(), gendervalue.get(), prebooking.get()}")
    
    with open("records.txt", "a") as f:
        f.write(f"The name of student is {namevalue.get()}\n")
        f.write(f"The age of student is {agevalue.get()}\n")
        f.write(f"The gender of student is {gendervalue.get()}\n")
        f.write(f"The prebooking of student is {prebooking.get()}\n\n")  # Added an extra newline for separation

root.geometry("600x600")
root.title("Dance Class")

# Labels
Label(root, text="Enter Your Name").grid(row=0, column=0)
Label(root, text="Enter Your Age").grid(row=1, column=0)
Label(root, text="Enter Your Gender").grid(row=2, column=0)

# Entry variables
namevalue = StringVar()
agevalue = StringVar()
gendervalue = StringVar()
prebooking = IntVar()  # For the Checkbutton

# Entries
Entry(root, textvariable=namevalue, width=30).grid(row=0, column=1)
Entry(root, textvariable=agevalue, width=30).grid(row=1, column=1)
Entry(root, textvariable=gendervalue, width=30).grid(row=2, column=1)

# Checkbutton
Checkbutton(root, text="Wanna do Pre Booking", variable=prebooking).grid(row=3, column=1)

# Submit Button (corrected line)
Button(root, text="Submit", command=getvals).grid(row=4, column=1)

root.mainloop()