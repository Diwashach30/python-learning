## revision of python classs

## variable

# name = "Diwash" 
# print(name)      ##we dont have to declare it as int or string or float cause in python code is dynamically typed.

# ##or either we can print as
# name = "Diwash"
# print(f"my name is {name}")



# number1 = 100
# number2 = 200

# sum = number1 + number2
# print(f"the sum is {sum}")


# #calculator using variable


# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))

# sum = num1 + num2
# sub = num1 - num2
# mul = num1 * num2
# div = num1 / num2 
# mod = num1 % num2
# cube = num1 **3
# intdiv = num1 // num2   #remove all the number after decimal


# print (f"the sum of two number is {sum}")
# print (f"the sub of two number is {sub} ")
# print (f"the mul of two number is  {mul} ")
# print (f"the div of two number is  {div} ")
# print (f"the mod of two number is {mod}")



### data types

## int = number without decimal point
# float = number with decimal point
# boolean or bool = true or False
# string = text 
# list [] = ordered and changeable.allow duplicate items
# tuple() = ordered and unchangeable . allow dups items
# set{} = unordered, unchangeable and unindexed. No dups items
# dict{} = key Value.
# none = none of the type.




# num1 = 50
# num2 = 30.5
# name = "diwash"


# print(type(num2))  # this will show float on output

# set = { "apple","banana"}

# print(type(name))




# fruits = ("apple" , "banana" , "mango")


# print(type(fruits))
# print(fruits[1])


## data types 

# total_students = 300 # int
# fees = 1250.50  # float

# is_present = True  # bool

# boarding_name = "himalayan sec boarding"  # str

# includes = ["playground", "AC" , "TT Board" , "Bus"]  #list

# located = (" ratangar " , "bakulahar" , "chitwan"  )

# phone_no = {
#     "no" : "986522222" ,
#     "mail": "di@gmail.com" 
# }

# best = {"sports" , "arts"}



# print(type(total_students))
# print(type(fees))
# print(type(is_present))
# print(type(boarding_name))
# print(type(includes))
# print(type(located))
# print(type(phone_no))
# print(type(best))


# expenses ={
#     "sun": "45.40",
#     "mon ": "55.60",
#     "tues ": "65.70"
    
    
    
    
# }


# total_expenses = sum(float(value) for value in expenses.values())

# print (f"{total_expenses:.2f}")



## condition
# temperature = int(input("enter current temperature:"))
# if temperature >= 25 :
#     print("wear shirt or tshirt")
# elif temperature >= 15 <= 25 :
#     print("wear pant")
# else :
#     print("put jackets and trouser")


## ASSERT morely used on testing purpose

# price = -50

# assert price >= 0, "Price must be positive"

# print("after assert")



# age = int(input("enter person age :"))

# assert age >= 0 , "age must be positive"

# print(f"after assert or age is {age}")


## LOOP
# for and while loop


# name = "diwash"


# for i in range(1,10):
#     print("diwash")


# for i in range (1,101):
#     if i % 2 == 0 :
#       print(i)
    
    
# names = ["ram " ,  "diwash" , "shyam"]

# for name in names :
#     print(name)   

# numbers = [1 ,2 ,3 , 4, 5] 
# total = 0

# for number in numbers:
#     total += number
#     print("total:", total)


# countdown = 6
# while countdown >1 :
#     countdown -= 1
#     print(countdown)
    
# print("countdown completed.")


# password = ""
# while password != "diwash123":    #the use of not equal is more in while in my opinion
#   password = input("enter password:")
# print("wow")



# for i in range(1,10) :
#    if  i == 6 :
#       break
#    print(i)



