print ("Stock management software")
print ("1. Add Product")
print ("2. View Product")
choice = int(input("Enter your choice: "))
adding = True

if choice == 1:
    print ("Add Product")
    name = input("Enter name: ")    
    quantity = int(input("Enter quantity: "))
    print (f"Name: {name}")
    print (f"Quantity: {quantity}")    
    file = open("stock.csv", "a")
    file.write(f"{name},{quantity}\n")
    file.close()
    
elif choice == 2:
    print ("View Product")
    file = open("stock.csv", "r")
    print (file.read())
    file.close()
    
question = input("Do you want to add more stock? [Yes/No]")
if question.lower() == "No":
    adding = False
else :
    choice = int(input("Enter your choice: (1.Add Product 2.View Product) "))