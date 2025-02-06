# Write a python program to create a class Laptop with properties [id, name, ram] and create 3 objects of it and print all details.

class Laptop:
     def __init__(self, id, name, ram):
      self.id = id
      self.name = name
      self.ram = ram
    
     def laptop_details(self):
      print(f"id: {self.id}")
      print(f"name: {self.name}")
      print(f"ram: {self.ram}")



laptop1 = Laptop(1, "Dell", 8)
laptop2 = Laptop(2, "Lenovo", 16)
laptop3 = Laptop(3, "Asus", 32)

laptop1.laptop_details()
laptop2.laptop_details()
laptop3.laptop_details()

