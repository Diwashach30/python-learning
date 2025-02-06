# # def sum_of_three_numbers(num1, num2, num3):   
# #     total = num1 + num2 + num3
# #     # Print the total
# #     print("The total sum is:", total)
# #     return total

# # number1 = 5
# # number2 = 10
# # number3 = 15

# # sum_of_three_numbers(number1, number2, number3)




# # a = int("10")
# # b = int("20") 

# # total = a + b 
# # print(total)



# # price calculator


# # price = int(input("ener a number :"))
# # person = int (input("enter total person : "))

# # prices = price / person


# # print(f"one need to pay {prices}")

# ##operators in python

# # + : add
# # - : minus
# # * : multiply
# # / : divide
# # % : Modulo 
# # // : divides and return the integer Value
# # ** : exponentiation (cube , square)

# # num1 = 10
# # num2 = 4

# # print(num1+num2)
# # print(num1-num2)
# # print(num1*num2)
# # print(num1/num2)
# # print(num1**num2)
# # print(num1//num2)
# # print(num1%num2)

# # == : equal
# # != : not equal
# # > : greater than
# # < : less than
# # >= : greater or equal


# # num1 = 10
# # num2 = 11


# # print(num1 > num2)


# # atm_user_id = 11
# # atm_user_pin = 6790


# # inputid = int(input("enter user id:"))
# # inputpin = int(input("enter user pin:"))


# # if atm_user_id == inputid and atm_user_pin == inputpin:    ##and merge both variable but or merge only one among many.
# #     print("login successful")
# # else:
# #     print("login failed")
    
    
# # userinput = input("enter a word :")

# # firstword = userinput.lower()[0]

# # if firstword == 'a' or firstword == 'e' or firstword == 'i'  or firstword == 'o' or firstword == 'u' :
# #     print(f"the word is vowel")
# # else:
# #     print(f"it is not vowel.")

# ##arithmetic operators

# # num1 = 10
# # num1 +=3   
# # num1  -=3
# # num1 *=4
# # num1 /=5                     ##this will print 13 by adding 3 in num1 sub in num1 and go on.

# # print(num1 )



# ## membership operators (with the use of in or not in)
# studs =["ram", "sita" , "shyam" ]

# is_sita_in_studs = "sita" in studs
# is_diwash_in_studs = "diwash " in studs
# is_anjal_not_in_studs ="anjal" not in studs


# print(f"sita : {is_sita_in_studs}.")
# print(f'diwash : {is_diwash_in_studs}.')
# print(f"is_anjal_not_in_studs : {is_anjal_not_in_studs}")

# studs =["ram", "sita" , "shyam" ]


# print("ram" in studs)
# print("diwash" in studs)


## user input

# name = input("what is your name? :")

# print(f"my name is{name}.")



# num1 = int(input("enter a number :"))
# num2 = int(input("enter another number :"))


# sum = num1 + num2
# cube = num1 **3

# print(f"the sum between two number is {cube}.")


##string


# name = "diwash"   #string
# name1 = 'ram'    # this is also string

# greetings = "hello" + name + " welcome to our service " + name1

# print(greetings)
 
 
 
name = "sharad ,nabin ,pawan"
name1 = "     diwash sharma acharya    "    

# print(name.lower())
# print(name.upper())               ## if you are using method it always have to be close with two ()
# print(name.capitalize())
# # print(f"{name1.split(" ")[0].capitalize()} {name1.split(" ")[1].capitalize()}")
# print(name1.title())                         

# print(name1.strip())                         ##str.strip()
# print(name1.replace("diwash" , "usha"))     ## str.replace(a ,b)

# lists = name.split(",")

# for name in lists:
#     print(name)

# import random


# random_num = random.randint(1 , 10)
# print(random_num)


# cards = ['ace' , 'paan' ,'Hukum']   #don't use ""

# random.shuffle(cards)
# print(cards[1])        # use [0] or [1]  or so on to denote if you just want to print 1st name 


## QR by PIP

import qrcode

number = int(input("enter your number :"))
img = qrcode.make(number)
type(img)     #qecode.image.pill.PillImage
img.save("some_file.png")















