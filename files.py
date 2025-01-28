## write a program that save your current address on address.txt

name = input("Enter your name : ")
address = input("Enter your address : ")

file = open("address.txt", "w") 
file.write(f"Name : {name}\n")
file.write(f"Address : {address}")
file.close()
print("Successful")