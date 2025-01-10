## Read file and print
f = open ("names.txt", "r")
## Add all names to list

names = f.readlines()
for i in range (len(names)):
    names[i] = names[i].strip("\n")
 
# make all uppercase
names = [r.upper() for r in names]
 
name = input ("Enter a name :")


if name.upper() in names :
    print (f"{name} is available")
    
else:
    print (f"{name} is not available")
    
    