## create a calculator using tkinter

import tkinter as tk


def button_click(value):
    current_expression = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_expression + value)

# Function to evaluate the expression and display the result
def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to clear the entry box
def button_clear():
    entry.delete(0, tk.END)

    

root = tk.Tk()
root.geometry("600x600")
root.title("Calculator")
root.wm_iconbitmap("download.ico")


# Entry widget to show the expression and result
entry = tk.Entry(root, width=20, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

# Creating buttons and adding them to the window
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=button_equal)
    elif text == "C":
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=button_clear)
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=lambda value=text: button_click(value))
    button.grid(row=row, column=col)


root.mainloop()







