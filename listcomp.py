#Write a program that takes a list of numbers and creates a new list containing the
#squares of all even numbers from the original list.


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [num ** 2 for num in numbers if num % 2 == 0]
print(squares)
