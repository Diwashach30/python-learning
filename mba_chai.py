import tkinter as tk
from tkinter import ttk, messagebox
import csv


ORDER_FILE = "tea_shop_orders.csv"

# Function to initialize the CSV file
def initialize_csv():
    try:
        with open(ORDER_FILE, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Table No", "Tea Types", "Quantities", "Total"])
    except FileExistsError:
        pass

# Add or Update Order
def add_or_update_order():
    table_no = table_no_entry.get().strip()
    tea_type = tea_type_combobox.get().strip()
    quantity = quantity_entry.get().strip()
    
    if not table_no or not tea_type or not quantity:
        messagebox.showerror("Error", "All fields are required!")
        return
    
    try:
        quantity = int(quantity)
    except ValueError:
        messagebox.showerror("Error", "Quantity must be an integer!")
        return
    
    # Prices for different tea types
    tea_prices = {
        "Black Tea": 50,
        "Green Tea": 40,
        "Milk Tea": 60,
        "Regular Chiya": 55,
        "Ginger Tea / Lemon Tea": 60,
        "Fresh Mint Tea": 70,
        "Earl Grey Tea": 60,
        "Hot Chocolate": 100,
        "Cappuccino": 220,
        "Latte": 250,
        "Mocha": 300,
        "Espresso": 150,
        "Americano": 200,
        "Flat White": 250,
        "Macchiato": 300,
        "Cafe Latte": 250,
        "Cafe Mocha": 300,
        "Peach Lemon Ice - Tea": 300,
    }
    
    price = tea_prices.get(tea_type, 0)
    item_total = price * quantity
    
    # Read existing orders
    rows = []
    updated = False
    try:
        with open(ORDER_FILE, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                if row[0] == table_no:  # If table number matches
                    tea_types = row[1].split(", ")
                    quantities = list(map(int, row[2].split(", ")))
                    
                    # Check if the tea type already exists
                    if tea_type in tea_types:
                        idx = tea_types.index(tea_type)
                        quantities[idx] += quantity  # Update quantity
                    else:
                        tea_types.append(tea_type)  # Add new tea type
                        quantities.append(quantity)  # Add new quantity
                    
                    # Recalculate total
                    totals = sum(tea_prices[t] * q for t, q in zip(tea_types, quantities))
                    
                    # Update row
                    row[1] = ", ".join(tea_types)
                    row[2] = ", ".join(map(str, quantities))
                    row[3] = str(totals)
                    updated = True
                
                rows.append(row)
        
        # If table number not found, add new row
        if not updated:
            rows.append([table_no, tea_type, str(quantity), str(item_total)])
        
        # Write updated rows back to the file
        with open(ORDER_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Table No", "Tea Types", "Quantities", "Total"])
            writer.writerows(rows)
        
        messagebox.showinfo("Success", "Order added/updated successfully!")
        refresh_table()  # Automatically refresh the table
        
    except FileNotFoundError:
        messagebox.showerror("Error", "No orders found!")

# List Orders
def list_orders():
    table.delete(*table.get_children())
    try:
        with open(ORDER_FILE, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                table.insert("", tk.END, values=(row[0], row[1], row[2], row[3]))
    except FileNotFoundError:
        messagebox.showerror("Error", "No orders found!")

# Remove Selected Entry
def remove_selected_entry():
    # Get the selected item from the Treeview
    selected_item = table.selection()
    if not selected_item:
        messagebox.showerror("Error", "Please select an entry to remove!")
        return
    
    # Get the details of the selected item
    selected_row = table.item(selected_item, "values")
    table_no, tea_types, quantities, total = selected_row
    
    # Read existing orders
    rows = []
    try:
        with open(ORDER_FILE, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                # Keep rows that don't match the selected entry
                if row[0] != table_no or row[1] != tea_types or row[2] != quantities or row[3] != total:
                    rows.append(row)
        
        # Write updated rows back to the file
        with open(ORDER_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Table No", "Tea Types", "Quantities", "Total"])
            writer.writerows(rows)
        
        messagebox.showinfo("Success", f"Entry for Table {table_no} has been removed!")
        refresh_table()  # Refresh the table display
        
    except FileNotFoundError:
        messagebox.showerror("Error", "No orders found!")


def refresh_table():
    list_orders()


root = tk.Tk()
root.title("CHAI GPT")  # Bold title
root.geometry("800x600")

# Set background color
root.configure(bg="#2ECC71")  

# Create Frames
input_frame = tk.Frame(root, bg="#f0f0f0")
input_frame.pack(pady=10)
table_frame = tk.Frame(root, bg="#f0f0f0")
table_frame.pack(pady=10, fill=tk.BOTH, expand=True)

# Input Fields
tk.Label(input_frame, text="Table No:", bg="#f0f0f0", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5)
table_no_entry = tk.Entry(input_frame, font=("Arial", 12))
table_no_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Tea Type:", bg="#f0f0f0", font=("Arial", 12)).grid(row=0, column=2, padx=5, pady=5)
tea_types = [
    "Black Tea",
    "Green Tea",
    "Milk Tea",
    "Regular Chiya",
    "Ginger Tea / Lemon Tea",
    "Fresh Mint Tea",
    "Earl Grey Tea",
    "Hot Chocolate",
    "Cappuccino",
    "Latte",
    "Mocha",
    "Espresso",
    "Americano",
    "Flat White",
    "Macchiato",
    "Cafe Latte",
    "Cafe Mocha",
    "Peach Lemon Ice - Tea"
]
tea_type_combobox = ttk.Combobox(input_frame, values=tea_types, state="readonly", font=("Arial", 12))
tea_type_combobox.grid(row=0, column=3, padx=5, pady=5)

tk.Label(input_frame, text="Quantity:", bg="#f0f0f0", font=("Arial", 12)).grid(row=0, column=4, padx=5, pady=5)
quantity_entry = tk.Entry(input_frame, font=("Arial", 12))
quantity_entry.grid(row=0, column=5, padx=5, pady=5)


tk.Button(input_frame, text="Add/Update Order", command=add_or_update_order, bg="#4CAF50", fg="white", font=("Arial", 12)).grid(row=1, column=0, columnspan=2, pady=10)
tk.Button(input_frame, text="Remove Selected Entry", command=remove_selected_entry, bg="#FF9800", fg="white", font=("Arial", 12)).grid(row=1, column=2, columnspan=4, pady=10)
columns = ("Table No", "Tea Types", "Quantities", "Total")
table = ttk.Treeview(table_frame, columns=columns, show="headings", style="Treeview")
style = ttk.Style()


style.configure("Treeview", background="#B3E5FC", foreground="#000000", fieldbackground="#B3E5FC", font=("Arial", 10))  # Soft blue background
style.configure("Treeview.Heading", font=("Arial", 12, "bold"))

for col in columns:
    table.heading(col, text=col)
    table.column(col, width=150, anchor=tk.CENTER)
table.pack(fill=tk.BOTH, expand=True)

# Populate Table on Startup
list_orders()

# Run the Application
root.mainloop()