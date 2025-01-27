items_price = {"Iphone11": 50000, "Iphone12": 60000, "Iphone13": 70000, "Iphone14": 80000, "Iphone15": 90000}
print(items_price)

items_price["Iphone16"] = 100000
print(items_price)
print(items_price["Iphone11"])

for key, value in items_price.items():
    print(f" The price of {key} : {value}")
    
for key in items_price.keys():
    print(key)
    
for value in items_price.values():
    print(value)
