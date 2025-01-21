##Say Good Morning to all friends from names.txt using def function.

f = open("names.txt", "r")

all_names = f.readlines()

for i in range(len(all_names)):
    all_names[i] = all_names[i].strip("\n").title()
     

def greet(n):
    print(f"Good Morning {n}.")

for x in all_names:
    greet(x)

