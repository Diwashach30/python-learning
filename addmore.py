print("Welcome to Diwash Shop")



total_price = 0
is_shop =True

while is_shop:
    price = float(input("Enter Price :"))
    total_price = total_price + price
    
    choice = input("Do you want to add more? [Yes/No]")
    if choice.lower() == "no" :
        is_shop = False
    
print(f" total price which is {total_price}")

    