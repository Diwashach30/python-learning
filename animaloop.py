# Write a python program to create a class Animal with properties [id, name, color].
# Create another class called Cat and extends it from Animal. 
# Add new properties sound in String. Create an object of a Cat and print all details.

class Animal:
    def __init__(self, id, name, color):
        self.id = id
        self.name = name
        self.color = color
        
    def animal_details(self):
        print(f"id: {self.id}")
        print(f"name: {self.name}")
        print(f"color: {self.color}")
        
class Cat(Animal):
    def __init__(self, id, name, color, sound):
        super().__init__(id, name, color)
        self.sound = sound
        
    def cat_details(self):
        print(f"id: {self.id}")
        print(f"name: {self.name}")
        print(f"color: {self.color}")
        print(f"sound: {self.sound}")
        
        
cat = Cat(1, "Tom", "White", "Meow")
print(cat.id)
print(cat.name)
print(cat.color)
print(cat.sound)
cat.cat_details()