# Write a python program to create a class House with properties [id, name, price]. Create a constructor of it and create 3 objects of it. Add them to the list and print all details.

class House:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
        
        
    def house_details(self):
        print(f"id: {self.id}")
        print(f"name: {self.name}")
        print(f"price: {self.price}")   
        
        
h1 = House(1, "House 1", 100000)
h2 = House(2, "House 2", 200000)
h3 = House(3, "House 3", 300000)

houses = [h1, h2, h3]

for house in houses:
    house.house_details()
    
