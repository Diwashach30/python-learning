import csv
import tkinter as tk
from tkinter import messagebox, ttk

# Function to display the menu options in a PrettyTable format
def display_menu():
    pass  # Not needed in GUI version

# Add Product
def add_product_gui():
    def save_product():
        id = id_entry.get()
        name = name_entry.get()
        qty = qty_entry.get()
        price = price_entry.get()

        if not id or not name or not qty or not price:
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            with open('bag_shop_data.csv', 'a', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow([id, name, qty, price])
            messagebox.showinfo("Success", "Product added successfully.")
            add_window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add product: {e}")

    # Create a new window for adding a product
    add_window = tk.Toplevel(root)
    add_window.title("Add Product")
    add_window.geometry("300x200")

    tk.Label(add_window, text="ID:").grid(row=0, column=0, padx=10, pady=5)
    id_entry = tk.Entry(add_window)
    id_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(add_window, text="Name:").grid(row=1, column=0, padx=10, pady=5)
    name_entry = tk.Entry(add_window)
    name_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(add_window, text="Quantity:").grid(row=2, column=0, padx=10, pady=5)
    qty_entry = tk.Entry(add_window)
    qty_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(add_window, text="Price:").grid(row=3, column=0, padx=10, pady=5)
    price_entry = tk.Entry(add_window)
    price_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Button(add_window, text="Save", command=save_product).grid(row=4, column=0, columnspan=2, pady=10)

# List Products
def list_products_gui():
    try:
        with open("bag_shop_data.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)  # Skip header row

            # Create a new window for listing products
            list_window = tk.Toplevel(root)
            list_window.title("List Products")
            list_window.geometry("600x400")

            # Create a Treeview widget
            tree = ttk.Treeview(list_window, columns=("ID", "Name", "Qty", "Price", "Total"), show="headings")
            tree.heading("ID", text="ID")
            tree.heading("Name", text="Name")
            tree.heading("Qty", text="Quantity")
            tree.heading("Price", text="Price")
            tree.heading("Total", text="Total")
            tree.pack(fill=tk.BOTH, expand=True)

            for line in csv_reader:
                total = float(line[2]) * float(line[3])
                tree.insert("", "end", values=(line[0], line[1], line[2], line[3], total))
    except FileNotFoundError:
        messagebox.showerror("Error", "No products found!")

# Delete Product
def delete_product_gui():
    def delete():
        id = id_entry.get()
        if not id:
            messagebox.showerror("Error", "ID is required!")
            return

        try:
            with open('bag_shop_data.csv', 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                rows = list(csv_reader)

            with open('bag_shop_data.csv', 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                deleted = False
                for row in rows:
                    if row[0] != id:
                        csv_writer.writerow(row)
                    else:
                        deleted = True
                if deleted:
                    messagebox.showinfo("Success", "Product deleted successfully.")
                    delete_window.destroy()
                else:
                    messagebox.showerror("Error", "Product not found!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete product: {e}")

    # Create a new window for deleting a product
    delete_window = tk.Toplevel(root)
    delete_window.title("Delete Product")
    delete_window.geometry("300x100")

    tk.Label(delete_window, text="ID:").grid(row=0, column=0, padx=10, pady=5)
    id_entry = tk.Entry(delete_window)
    id_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Button(delete_window, text="Delete", command=delete).grid(row=1, column=0, columnspan=2, pady=10)

# Update Product
def update_product_gui():
    def update():
        id = id_entry.get()
        name = name_entry.get()
        qty = qty_entry.get()
        price = price_entry.get()

        if not id or not name or not qty or not price:
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            with open('bag_shop_data.csv', 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                rows = list(csv_reader)

            with open('bag_shop_data.csv', 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                updated = False
                for row in rows:
                    if row[0] == id:
                        row[1] = name
                        row[2] = qty
                        row[3] = price
                        updated = True
                    csv_writer.writerow(row)
                if updated:
                    messagebox.showinfo("Success", "Product updated successfully.")
                    update_window.destroy()
                else:
                    messagebox.showerror("Error", "Product not found!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update product: {e}")

    # Create a new window for updating a product
    update_window = tk.Toplevel(root)
    update_window.title("Update Product")
    update_window.geometry("300x200")

    tk.Label(update_window, text="ID:").grid(row=0, column=0, padx=10, pady=5)
    id_entry = tk.Entry(update_window)
    id_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(update_window, text="Name:").grid(row=1, column=0, padx=10, pady=5)
    name_entry = tk.Entry(update_window)
    name_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(update_window, text="Quantity:").grid(row=2, column=0, padx=10, pady=5)
    qty_entry = tk.Entry(update_window)
    qty_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(update_window, text="Price:").grid(row=3, column=0, padx=10, pady=5)
    price_entry = tk.Entry(update_window)
    price_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Button(update_window, text="Update", command=update).grid(row=4, column=0, columnspan=2, pady=10)

# Search Product
def search_product_gui():
    def search():
        nameini = name_entry.get()
        if not nameini:
            messagebox.showerror("Error", "Name is required!")
            return

        try:
            with open('bag_shop_data.csv', 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                rows = [row for row in csv_reader if row[1][0].upper() == nameini[0].upper()]

            if rows:
                # Create a new window for displaying search results
                search_window = tk.Toplevel(root)
                search_window.title("Search Results")
                search_window.geometry("600x400")

                # Create a Treeview widget
                tree = ttk.Treeview(search_window, columns=("ID", "Name", "Qty", "Price", "Total"), show="headings")
                tree.heading("ID", text="ID")
                tree.heading("Name", text="Name")
                tree.heading("Qty", text="Quantity")
                tree.heading("Price", text="Price")
                tree.heading("Total", text="Total")
                tree.pack(fill=tk.BOTH, expand=True)

                for row in rows:
                    total = float(row[2]) * float(row[3])
                    tree.insert("", "end", values=(row[0], row[1], row[2], row[3], total))
            else:
                messagebox.showinfo("Info", "No products found matching the criteria.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to search products: {e}")

    # Create a new window for searching a product
    search_window = tk.Toplevel(root)
    search_window.title("Search Product")
    search_window.geometry("300x100")

    tk.Label(search_window, text="Name Initial:").grid(row=0, column=0, padx=10, pady=5)
    name_entry = tk.Entry(search_window)
    name_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Button(search_window, text="Search", command=search).grid(row=1, column=0, columnspan=2, pady=10)

# Main Application Window
root = tk.Tk()
root.title("ABC Bagshop Software")
root.geometry("400x300")

tk.Label(root, text="Welcome to ABC Bagshop Software", font=("Arial", 16)).pack(pady=10)

tk.Button(root, text="Add Product", command=add_product_gui, width=20).pack(pady=5)
tk.Button(root, text="List Products", command=list_products_gui, width=20).pack(pady=5)
tk.Button(root, text="Delete Product", command=delete_product_gui, width=20).pack(pady=5)
tk.Button(root, text="Update Product", command=update_product_gui, width=20).pack(pady=5)
tk.Button(root, text="Search Product", command=search_product_gui, width=20).pack(pady=5)

root.mainloop()