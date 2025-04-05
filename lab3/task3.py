import math
from abc import abstractmethod, ABC


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2*(self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2*3.14*self.radius

class Triangle(Shape):
    def __init__(self, first_side, second_side, third_side):
        self.first_side = first_side
        self.second_side = second_side
        self.third_side = third_side
    def area(self):
        p = round(self.perimeter() / 2, 2)
        return math.sqrt(p * (p-self.first_side) * (p-self.second_side) * (p-self.third_side))

    def perimeter(self):
        return self.first_side + self.second_side + self.third_side

shape = [Rectangle(10, 20), Circle(4), Triangle(3,4,5)]

def print_shape_info(shape):
    for i in shape:
        print(f"Площадь равна {i.area()}. Периметр равен {i.perimeter()}")

print_shape_info(shape)