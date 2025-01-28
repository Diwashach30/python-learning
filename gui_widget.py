# gui just for last bar typing ready as a text

import tkinter as tk

root = tk.Tk()
root.title("READY")


footer_label = tk.Label(root, text="READY" , font=("Arial", 12), fg="green" , bg="black",)
footer_label.pack(side=tk.BOTTOM, pady=10)




root.mainloop()