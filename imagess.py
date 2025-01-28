#display image with user of GUI and kinter


from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Image Viewer")
root.geometry("600x600")
root.config(bg="#F5F5F5")  # Light gray background



# Load and display the image
image = Image.open("2.jpg")
image = image.resize((600, 600))  # Resize the image to fit the canvas
photo = ImageTk.PhotoImage(image)

image_label = Label(root, image=photo, bg="#F5F5F5") 
image_label.pack(pady=10)

root.mainloop()



