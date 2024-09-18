# Here the polymorphism concept is there
class Shape:
    def print_area_of_shape(self):
        raise NotImplementedError("Subclasses will implement this function!")


class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def print_area_of_shape(self):
        area = self.length * self.breadth
        print(f"Area of rectangle is {area}")

class Circle:
    def __init__(self,radius):
        self.radius = radius
    def print_area_of_shape(self):
        area = self.radius * self.radius * 3.14
        print(f"Area of circle is {area}")

r1 = Rectangle(12,23)
c1 = Circle(2)
r1.print_area_of_shape()
c1.print_area_of_shape()
