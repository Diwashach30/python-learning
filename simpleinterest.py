import tkinter as tk
from tkinter import font

def calculate():
    try:
        principle = float(textbox1.get())
        time = float(textbox2.get())  # in hours
        rate = float(textbox3.get())
        
        simple_interest = (principle * time * rate) / 100
        result_label.config(text=f"Simple Interest: Rs {simple_interest:.2f}", fg="#4CAF50")
    except ValueError:
        result_label.config(text="Please enter valid numbers!", fg="#FF0000")

root = tk.Tk()
root.title("Simple Interest Calculator")
root.geometry("600x600")
root.config(bg="#F5F5F5")  # Light gray background

# Center window
root.eval('tk::PlaceWindow %s center' % root.winfo_toplevel())

# Use a modern font for labels and textboxes
font_large = font.Font(family="Segoe UI", size=14)
font_button = font.Font(family="Segoe UI", size=12, weight="bold")

# Add a gradient background
canvas = tk.Canvas(root, height=600, width=600, bg="#F5F5F5", highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Gradient color
canvas.create_rectangle(0, 0, 600, 600, fill="#F5F5F5", outline="")

# Labels
label1 = tk.Label(root, text="Principle:", font=font_large, bg="#F5F5F5", anchor="w", padx=10)
label1.place(relx=0.1, rely=0.1, relwidth=0.8, height=35)

textbox1 = tk.Entry(root, font=font_large, bd=2, relief="flat", highlightthickness=2, highlightbackground="#E0E0E0", bg="#FFFFFF")
textbox1.place(relx=0.1, rely=0.2, relwidth=0.8, height=40)

label2 = tk.Label(root, text="Time (in hours):", font=font_large, bg="#F5F5F5", anchor="w", padx=10)
label2.place(relx=0.1, rely=0.3, relwidth=0.8, height=35)

textbox2 = tk.Entry(root, font=font_large, bd=2, relief="flat", highlightthickness=2, highlightbackground="#E0E0E0", bg="#FFFFFF")
textbox2.place(relx=0.1, rely=0.4, relwidth=0.8, height=40)

label3 = tk.Label(root, text="Rate (%):", font=font_large, bg="#F5F5F5", anchor="w", padx=10)
label3.place(relx=0.1, rely=0.5, relwidth=0.8, height=35)

textbox3 = tk.Entry(root, font=font_large, bd=2, relief="flat", highlightthickness=2, highlightbackground="#E0E0E0", bg="#FFFFFF")
textbox3.place(relx=0.1, rely=0.6, relwidth=0.8, height=40)

# Calculate button with smooth hover effect
def on_enter(event):
    button1.config(bg="#4CAF50")

def on_leave(event):
    button1.config(bg="#45a049")

button1 = tk.Button(root, text="Calculate", font=font_button, fg="white", bg="#45a049", bd=0, relief="flat", command=calculate)
button1.place(relx=0.1, rely=0.75, relwidth=0.8, height=50)
button1.bind("<Enter>", on_enter)
button1.bind("<Leave>", on_leave)

# Result label with styling
result_label = tk.Label(root, text="", font=font_large, bg="#F5F5F5", fg="#4CAF50")
result_label.place(relx=0.1, rely=0.85, relwidth=0.8, height=35)

root.mainloop()