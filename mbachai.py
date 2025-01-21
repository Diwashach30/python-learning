import tkinter as tk
def calculate():
    chiya = int(textbox1.get())
    biscuit = int(textbox2.get()) 
    pakauda = int(textbox3.get())   
    others = int(textbox4.get())
    
    
    total_amount = chiya + biscuit + pakauda + others 
    result_label.config(text=f"Total Amount is Rs {total_amount}")
    
    

root = tk.Tk()

root.title("MBA CHAI (Table 1)")
root.geometry("900x600")

label1 = tk.Label(root, text="Chiya : ")
label1.pack()



textbox1 = tk.Entry(root)
textbox1.pack(pady=10)


label2 = tk.Label(root, text="Biscuit: ")
label2.pack()

textbox2 = tk.Entry(root)
textbox2.pack(pady=10)

label3 = tk.Label(root, text="Pakauda: ")
label3.pack()

textbox3 = tk.Entry(root)
textbox3.pack(pady=10)

label4 = tk.Label(root, text="Others: ")
label4.pack()

textbox4 = tk.Entry(root)
textbox4.pack(pady=10)


button1 = tk.Button(root, text = "Calculate", command=calculate)
button1.pack()


result_label = tk.Label(root, text="")
result_label.pack()


root.mainloop()