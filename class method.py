class Employee:
    #var of class
    increment = 2.3
    no_of_employees=0
    def __init__(self , fname , lname , salary): #this take object as an argument
        #var of names
        self.name1 = fname
        self.name2 =lname
        self.pay = salary
        # self.increment=3.5
        Employee.no_of_employees+=1
    def increase(self):
        self.pay= int (self.pay * Employee.increment)

        #if we are concerned with vars of class..wanna chg n update suppose
    @classmethod
    def change_increment(cls , amount):
        cls.increment = amount

    @classmethod
    def from_str(cls , emp_str):
     fname , lname , salary = emp_str.split("-")
     return cls ( fname , lname , salary)

    # idependent function
    @staticmethod
    def isopen(day):
        if day=="sunday":
            return False
        else:
            return True

#INHERITANCE
class Programmer(Employee):
    def __init__(self , fname , lname , salary , proglang  , exp):
        super().__init__(fname , lname , salary)
        self.proglang = proglang
        self.exp = exp

    def increase(self):
        self.pay= int (self.pay * (self.increment + 0.2 ) )
        return self.pay




print(Employee.no_of_employees)
harry= Employee("harry", "jack", 3300)
rohan= Employee("rohan", "william", 3300)
print(Employee.no_of_employees)
harry.increase()
print(harry.pay)
Employee.change_increment(3)
harry.increase()
print(harry.pay)
# print(Employee.isopen("Monday"))
omer = Programmer("Omer" , "Ali" , 3300 , "python" , "4 years")
omer.increase()
print(omer.pay)   # 8250
help(Programmer)
print(omer.increase())


 #class method somrtimes treated as constructor

lovish = Employee.from_str("harry - jack - 3300")
print(lovish.name2)
        #idependent function



