country_capital = {"Nepal": "Kathmandu", "India": "Delhi", "Pakistan": "Islamabad", "Bangladesh": "Dhaka"}

print(list(country_capital.keys()))
print(list(country_capital.values()))
print(country_capital["Nepal"])

for key, value in country_capital.items():
    print(f"{value} is the capital of {key}")