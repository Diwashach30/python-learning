print("Student Management Software")
print("1. Add Student")
print("2. View Student")
choice = int(input("Enter your choice: "))
adding = True

if choice == 1:
    print("Add Student")
    name = input("Enter name: ")    
    age = int(input("Enter age: "))
    address = input("Enter address: ")
    print(f"Name: {name}")
    print(f"Age: {age}")    
    file = open("student.csv", "a")
    file.write(f"{name},{age} , {address}\n")
    file.close()
    
elif choice == 2:
    print("View Student")
    file = open("student.csv", "r")
    print(file.read())
    file.close()
    
question = input("Do you want to add more student? [Yes/No]")
if question.lower() == "No":
    adding = False
else :
    choice = int(input("Enter your choice: (1.Add Student 2.View Student) "))