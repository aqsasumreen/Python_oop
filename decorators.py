# Decorators are implemented using functions themselves.
# They take another function as an argument, add some kind of functionality,
# and then return the original function or a new function that incorporates
# the added functionality.

class Employee:
    #var of class
    increment = 2.3
    no_of_employees=0
    def __init__(self , fname , lname , salary): #this take object as an argument
        #var of names
        self.name1 = fname
        self.name2 =lname
        self.pay = salary
        # self.email = fname +lname +"@gmail.com"
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
    @property
    def email(self):
        if self.name1 == None:
            return "email not set"
        else:
            return self.name1 +"." + self.name2 + "@gmail.com"
    @email.setter
    def email(self , given_email):
        nameList = given_email.split("@")[0].split(".")
        print(nameList)
        self.name1 =nameList[0]
        self.name2 =nameList[1]
    @email.deleter
    def email(self):
        self.name1 = None
        self.name2 = None


if __name__ == '__main__':
    harry= Employee("harry", "jack", 3300)
    rohan= Employee("rohan", "william", 3300)
    print(harry.email ,"\n" , rohan.email)
    rohan.name2 = "mughal"
    print(rohan.email)
    #if user wannna change email then
    rohan.email = "mughal.rohan@gmail.com"
    print( rohan.email)
    del rohan.email
    print(rohan.email)




