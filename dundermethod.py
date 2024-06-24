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
        #dunder method
    def __add__(self, other):
        return self.pay+other.pay

    def __repr__(self):
        return "Employee ({} , {} , {})".format(self.name1 , self.name2 , self.pay)
    def __str__(self):
        return "{}  last name is {}" .format(self.name1 , self.name2)

harry= Employee("harry", "jack", 3300)
rohan= Employee("rohan", "william", 3300)
a="aqsa"
print(a.__add__(" sumreen"))
print(harry+rohan)
print(repr(harry))
print(str(rohan))

