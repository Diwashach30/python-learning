import random
print ("Three Lucky Winners")

f = open("names.txt", "r")

names = f.readlines()

lucky_one = random.choice(names)
print(f"First winner is {lucky_one}")
def greet(lucky_one):
    print(f"Good Morning {lucky_one}")
    
greet(lucky_one)
names.remove(lucky_one)
lucky_two = random.choice(names)
print(f"Second winner is {lucky_two}")

def greet(lucky_two):
    print(f"Good Morning {lucky_two}")
    
greet(lucky_two)
names.remove(lucky_two)
lucky_three = random.choice(names)
print(f"Third winner is {lucky_three}")

def greet(lucky_three):
    print(f"Good Morning {lucky_three}")
    
greet(lucky_three)
names.remove(lucky_three)







