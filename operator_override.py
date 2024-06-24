class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def area(self):
        return self.x * self.y


class Circle(Shape):
   def __init__(self, radius):
       self.radius = radius

   def area(self):
       return  3.14*self.radius * self.radius

a1 = Circle(7)
print(a1.area())