import tkinter as tk
def calculate():
    total_amount = float(textbox1.get())
    total_person = float(textbox2.get())
    
    
    amount_per_person = total_amount / total_person
    result_label.config(text=f"Each person need to pay Rs {amount_per_person:.2f}")
    
    

root = tk.Tk()

root.title("Diwash Bill Split Software")
root.geometry("900x600")
label1 = tk.Label(root, text="Enter Total Amount: ")
label1.pack()



textbox1 = tk.Entry(root)
textbox1.pack(pady=10)


label2 = tk.Label(root, text="Enter Total People: ")
label2.pack()

textbox2 = tk.Entry(root)
textbox2.pack(pady=10)

button1 = tk.Button(root, text = "Calculate", command=calculate)
button1.pack()


result_label = tk.Label(root, text="")
result_label.pack()


root.mainloop()