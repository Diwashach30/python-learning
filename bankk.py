## bank software

class Customer :
    def __init__(self,acno,name,balance):
        self.acno = acno
        self.name = name ,
        self.balance = balance
        
        
    def deposit(self, amount):
        self.balance += amount
        
        
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient Balance")
        self.balance -= amount
        
        
    def display_balance(self):
        print(f"Account Number : {self.acno}")
        print(f"Name: {self.name}")
        print(f"Balance : {self.balance}")
        
        
customer1 = Customer(11 , "diwash sharma " ,0)
customer2 = Customer(12 , "Biswo Paudel" , 1600)
customer1.deposit(600)
customer1.withdraw(200)
customer1.display_balance()
    