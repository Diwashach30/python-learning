from tkinter import *

root = Tk()
root.geometry("600x600")
root.title("Scrollbar")


scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

Listbox = Listbox(root , yscrollcommand= scrollbar.set)
for i in range(100):
    Listbox.insert(END, "Item " + str(i))
Listbox.pack(fill=BOTH, expand=1)
# text =Text(root, yscrollcommand= scrollbar.set)
# text.pack(fill=BOTH)
    
scrollbar.config(command=Listbox.yview)






root.mainloop()