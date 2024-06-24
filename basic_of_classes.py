class Employee:
    #var of class
    increment = 2.3
    no_of_employees=0
    def __init__(self , fname , lname , salary): #this take object as an argument
        #var of names
        self.name1 = fname
        self.name2 =lname
        self.pay = salary
        self.increment=3.5
        Employee.no_of_employees+=1
    def increase(self):
        self.pay= int (self.pay * Employee.increment)


print(Employee.no_of_employees)
harry= Employee("harry", "jack", 3300)
rohan= Employee("rohan", "william", 3300)
print(Employee.no_of_employees)
print(harry.name1 , rohan.name2)
harry.increase()
print("harry`s increment" , harry.pay)
rohan.increase()
print("Rohan`s increment" , rohan.pay)
print(harry.__dict__)
rohan.increment=8.9
rohan.increase()
print("Rohan`s  new increment" , rohan.pay)
print(rohan.__dict__)
print(Employee.__dict__)

#class method take class as an
# str =  " this is my book. "
# print(str[: : -1])
# class Book:
#     pass
#
# p1 = Book()
