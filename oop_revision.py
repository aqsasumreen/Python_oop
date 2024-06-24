class Person:
    def __init__(self, name, occupation):  # two types  : parameterized and default
        print("I`m constructor i run when obj is created.")
        self.name = name
        self.occ = occupation

    def show(self):
        print(f"I`m {self.name} and my occupation is  {self.occ}")


a = Person("Aqsa", "Development")
a.show()


# --------------------> Decorators <--------------------
# "Suppose we want to display a message at the beginning and end of a function.
# We can modify the function in one way, but we'll create a function that
# takes another function as an argument and calls it."
# ===> Decorator
def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thanks for using ,, Im the last msg")

    return mfx


# ===> one way of using decorator is :
# @greet
def hello():
    print("HELLO Im function without arguments")


@greet
def add(a, b):
    print("Function with arguments", a + b)


# hello()
# Another way of using decorator is :
greet(hello)()

add(9, 9)


# Now for a function with arguments we used args and kwargs

# ======>Name Mangling
# Its a technique that is used to protect class private and
# superClass private members from being accidentally overwritten.,


class Student:
    def __init__(self):
        self.__name = "Im private"  # private ,, but main thing is mangling used with -> __ <--

    def _funcName(self):  # protected function
        return "Im function"


# class Subject(Student):
#     pass

# obj = Subject()
obj1 = Student()
print(obj1.__dir__())
print(obj1.__dict__)  # vars ki dictionary bna k de ga.
print(help(Student))  # Person class me jo kuch ho ga sb btaye ga
# print(obj1._funcName())

# print(obj1._Student__name) # mangling
