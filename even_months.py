import calendar
year = int(input("Enter Year : "))

for i in range (1,13):
    if i % 2 == 0 :

         print(calendar.month(year,i))