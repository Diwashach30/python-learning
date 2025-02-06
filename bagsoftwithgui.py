import csv
from tkinter import *
from tkinter import messagebox, ttk

# File path for the CSV file
CSV_FILE = "bag_shop_data.csv"

# Initialize the CSV file if it doesn't exist
def initialize_csv():
    try:
        with open(CSV_FILE, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Qty", "Price"])
    except FileExistsError:
        pass

# Add Product
def add_product():
    id = id_entry.get()
    name = name_entry.get()
    qty = qty_entry.get()
    price = price_entry.get()

    if not id or not name or not qty or not price:
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        qty = int(qty)
        price = float(price)
    except ValueError:
        messagebox.showerror("Error", "Quantity must be an integer and Price must be a float!")
        return

    with open(CSV_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id, name, qty, price])
    
    messagebox.showinfo("Success", "Product added successfully!")
    clear_entries()
    refresh_table()

# List Products
def list_products():
    table.delete(*table.get_children())
    try:
        with open(CSV_FILE, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                total = float(row[2]) * float(row[3])
                table.insert("", END, values=(row[0], row[1], row[2], row[3], total))
    except FileNotFoundError:
        messagebox.showerror("Error", "No products found!")

# Search Product
def search_product():
    query = search_entry.get().strip()
    if not query:
        messagebox.showerror("Error", "Please enter a product name to search!")
        return

    table.delete(*table.get_children())
    try:
        with open(CSV_FILE, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            found = False
            for row in reader:
                if query.lower() in row[1].lower():
                    total = float(row[2]) * float(row[3])
                    table.insert("", END, values=(row[0], row[1], row[2], row[3], total))
                    found = True
            if not found:
                messagebox.showinfo("Info", "No matching products found!")
    except FileNotFoundError:
        messagebox.showerror("Error", "No products found!")

# Update Product
def update_product():
    id = id_entry.get()
    name = name_entry.get()
    qty = qty_entry.get()
    price = price_entry.get()

    if not id or not name or not qty or not price:
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        qty = int(qty)
        price = float(price)
    except ValueError:
        messagebox.showerror("Error", "Quantity must be an integer and Price must be a float!")
        return

    updated = False
    rows = []
    try:
        with open(CSV_FILE, 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            for row in rows:
                if row[0] == id:
                    row[1], row[2], row[3] = name, str(qty), str(price)
                    updated = True
                    break

        if not updated:
            messagebox.showerror("Error", "Product ID not found!")
            return

        with open(CSV_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        messagebox.showinfo("Success", "Product updated successfully!")
        clear_entries()
        refresh_table()
    except FileNotFoundError:
        messagebox.showerror("Error", "No products found!")

# Delete Product
def delete_product():
    id = id_entry.get()
    if not id:
        messagebox.showerror("Error", "Please enter a Product ID to delete!")
        return

    deleted = False
    rows = []
    try:
        with open(CSV_FILE, 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            for row in rows:
                if row[0] == id:
                    rows.remove(row)
                    deleted = True
                    break

        if not deleted:
            messagebox.showerror("Error", "Product ID not found!")
            return

        with open(CSV_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        messagebox.showinfo("Success", "Product deleted successfully!")
        clear_entries()
        refresh_table()
    except FileNotFoundError:
        messagebox.showerror("Error", "No products found!")

# Clear Input Fields
def clear_entries():
    id_entry.delete(0, END)
    name_entry.delete(0, END)
    qty_entry.delete(0, END)
    price_entry.delete(0, END)

# Refresh Table
def refresh_table():
    list_products()

# Main Application Window
root = Tk()
root.title("ABC Bagshop Software")
root.geometry("800x600")

# Initialize CSV file
initialize_csv()

# Create Frames
input_frame = Frame(root)
input_frame.pack(pady=10)

table_frame = Frame(root)
table_frame.pack(pady=10, fill=BOTH, expand=True)

# Input Fields
Label(input_frame, text="ID:").grid(row=0, column=0, padx=5, pady=5)
id_entry = Entry(input_frame)
id_entry.grid(row=0, column=1, padx=5, pady=5)

Label(input_frame, text="Name:").grid(row=0, column=2, padx=5, pady=5)
name_entry = Entry(input_frame)
name_entry.grid(row=0, column=3, padx=5, pady=5)

Label(input_frame, text="Quantity:").grid(row=0, column=4, padx=5, pady=5)
qty_entry = Entry(input_frame)
qty_entry.grid(row=0, column=5, padx=5, pady=5)

Label(input_frame, text="Price:").grid(row=0, column=6, padx=5, pady=5)
price_entry = Entry(input_frame)
price_entry.grid(row=0, column=7, padx=5, pady=5)

# Buttons
Button(input_frame, text="Add Product", command=add_product).grid(row=1, column=0, columnspan=2, pady=10)
Button(input_frame, text="Update Product", command=update_product).grid(row=1, column=2, columnspan=2, pady=10)
Button(input_frame, text="Delete Product", command=delete_product).grid(row=1, column=4, columnspan=2, pady=10)

# Search Bar
search_frame = Frame(root)
search_frame.pack(pady=10)

Label(search_frame, text="Search by Name:").pack(side=LEFT, padx=5)
search_entry = Entry(search_frame)
search_entry.pack(side=LEFT, padx=5)
Button(search_frame, text="Search", command=search_product).pack(side=LEFT, padx=5)
Button(search_frame, text="Refresh", command=refresh_table).pack(side=LEFT, padx=5)

# Table
columns = ("ID", "Name", "Qty", "Price", "Total")
table = ttk.Treeview(table_frame, columns=columns, show="headings")
for col in columns:
    table.heading(col, text=col)
    table.column(col, width=100, anchor=CENTER)
table.pack(fill=BOTH, expand=True)

# Populate Table on Startup
list_products()

# Run the Application
root.mainloop()