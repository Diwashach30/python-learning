f = open("names.txt", "r")

names = f.readlines()
for  i in range(len(names)):
    names[i] = names[i].strip("\n")

def greet(n):
    print(f"Good Morning {n}")
    
for name in names:
    greet(name)