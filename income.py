###list of income

jan = int(input("enter january income: "))
feb = int(input("enter february income: "))
march = int(input("enter march income: "))
april = int(input("enter April income: "))
may = int(input("enter may income: "))
june = int(input("enter june income: "))
july = int(input("enter july income: "))
aug = int(input("enter august income: "))
sept = int(input("enter september income: "))
oct = int(input("enter Oct income: "))
nov= int(input("enter nov income: "))
december = int(input("enter december income: "))

total_income = jan+feb+march+april+may+june+july+aug+sept+oct+nov+december

average_income = total_income / 12
  
  
print(f"Hence total income is Rs {total_income:.2f}")
print(f"Hence average income  is Rs {average_income:.2f}")




