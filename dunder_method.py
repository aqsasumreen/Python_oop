# also known as "magic" or "special" methods. These methods are special because
# they are surrounded by double underscores (__) at the beginning and end of
# their names. They allow Python classes to emulate built-in types or
# provide special functionality.

class Users:
    increment = 1.5

    def __init__(self, name, password):
        self.name = name
        self.password = password

    #  self waly instance k  vars hty ,,class k nhi
    # aqsa , ali instances  hy
    # self.name mean aqsa.name
    def increase(self):
        self.password = int(self.password * self.increment)

    # CLass method which takes class as an argument
    @classmethod
    def incoming(cls, amount):
        cls.increment = amount

    #         CLASS METHOD AS CONSTRUCTOR
    @classmethod
    def from_str(cls, aik_str):
        name, password = aik_str.split("-")
        return cls(name, password)

    @staticmethod
    def chk(day):
        if day == "sunday":
            return False
        else:
            return True

    def __add__(self, other):
        return self.password + other.password

    def __repr__(self):
        return "Users({} , {} )".format(self.name, self.password)

    def __str__(self):
        return "The name of User is {}".format(self.name)

    def __call__(self):  # obj ko as function call krny pr run ho ga.
        return "Im call method"


aqsa = Users("Aqsa", 8800)
ali = Users("Alii", 9900)
print(aqsa + ali)  # operator overload , e.g __sub__ , __Mul__
print(repr(ali))
print(ali)  # Str run ho ga ,,,agr str nhi bna tou repr chly ga
print(aqsa())
