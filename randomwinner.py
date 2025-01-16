import random
print ("Three Lucky Winners")

f = open("names.txt", "r")

names = f.readlines()

lucky_one = random.choice(names)
print(f"First winner is {lucky_one}")
names.remove(lucky_one)
lucky_two = random.choice(names)
print(f"Second winner is {lucky_two}")
names.remove(lucky_two)
lucky_three = random.choice(names)
print(f"Third winner is {lucky_three}")
names.remove(lucky_three)


print(f"Good Luck for next time :")

for remaining_name in names:
    print(f"{remaining_name}")



