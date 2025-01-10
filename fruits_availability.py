fruits = ['Apple', 'Orange', 'Mango']

fruits = [fruit.upper() for fruit in fruits]

fruit_name = input("Enter a fruit name")
if fruit_name in fruits :
    print(f"{fruit_name} is available")
else:
    print(f"{fruit_name} is not available")