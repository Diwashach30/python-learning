import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# Create main application window
root = tk.Tk()
root.title("Notepad")
root.geometry("600x400")


text_area = tk.Text(root, wrap="word", undo=True)
text_area.pack(expand="yes", fill="both")


def new_file():
    text_area.delete(1.0, tk.END)


def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())


def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, tk.END))

def exit_app():
    if messagebox.askyesno("Exit", "Do you really want to exit?"):
        root.quit()


menu_bar = tk.Menu(root)
root.config(menu=menu_bar)


file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)


root.mainloop()
