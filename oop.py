## create 3 obj with claass teacher

class Teacher:
    def __init__(self,firstname,middlename,lastname):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
       
       
    def full_name(self):
        print(f"{self.firstname} {self.middlename} {self.lastname}")
        
        

t1 = Teacher("Diwash","Sharma","Acharya")
t2 = Teacher("Som","Prakash","Chaudary")
t3 = Teacher("Bishwo", "","Paudel")

t1.full_name()
t2.full_name()
t3.full_name()