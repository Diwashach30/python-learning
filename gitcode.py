def check_voter(age):
    if age >= 18:
        return "Voter"
    else:
        return "Not Voter"

# Example usage
if __name__ == "__main__":
    age = int(input("Enter your age: "))
    result = check_voter(age)
    print(result)