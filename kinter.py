## understanding all basics of Tk
import tkinter as tk
from tkinter.ttk import Label  #where tk stands for tool kit ar it is just a library which incluses all the widgets, tools labels etc

root = tk.Tk()# where root is the main window where root variable got permission to place all the tools from the tkinter library
root.geometry("733x434")

root.minsize(300,100)

root.maxsize(1200,988)

diwash = tk.Label(text="Diwash is a good boy and is learning python.")
diwash.pack()



root.mainloop() # which helps to create a blank window or main window in the background where we are supposed to 
    # place all the widgets, tool kits etc and keep it on a loop so that the window will not close
    



