import tkinter as tk
def calculate():
    principle = float(textbox1.get())
    time = float(textbox2.get())        ##in_hour
    rate = float(textbox3.get())
    
    
    simple_interest = (principle * time * rate ) / 100
    result_label.config(text=f"SI is Rs {simple_interest:.2f}")
    
    

root = tk.Tk()

root.title("Simple Interest Calculator")
root.geometry("900x600")

label1 = tk.Label(root, text="Principle : ")
label1.pack()



textbox1 = tk.Entry(root)
textbox1.pack(pady=10)


label2 = tk.Label(root, text="Time: ")
label2.pack()

textbox2 = tk.Entry(root)
textbox2.pack(pady=10)

label3 = tk.Label(root, text="Rate: ")
label3.pack()

textbox3 = tk.Entry(root)
textbox3.pack(pady=10)

button1 = tk.Button(root, text = "Calculate", command=calculate)
button1.pack()


result_label = tk.Label(root, text="")
result_label.pack()


root.mainloop()