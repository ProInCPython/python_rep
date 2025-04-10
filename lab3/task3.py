import math
from abc import abstractmethod, ABC


class Shape(ABC):
    """Абстрактный класс Shape.

    Methods
    -------
    area()
        абстрактный метод вычисления площади
    perimeter()
        абстрактный метод вычисления периметра
    """

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    """Класс Rectangle, наследующий класс Shape.

    Attributes
    ----------
    width : float
        длина прямоугольника
    height : float
        высота прямоугольника

    Methods
    -------
    area() -> float
        вычисляет площадь прямоугольника
    perimeter() -> float
        вычисляет периметр прямоугольника
    """

    def __init__(self, width : float, height : float):
        self.width = width
        self.height = height

    def area(self) -> float:
        """Верни площадь прямоугольника."""

        return self.width * self.height

    def perimeter(self) -> float:
        """Верни периметр прямоугольника."""

        return 2*(self.width + self.height)

class Circle(Shape):
    """Класс Circle, наследующий класс Shape.

    Attributes
    ----------
    radius : float
        радиус круга

    Methods
    -------
    area() -> float
        вычисляет площадь круга
    perimeter() -> float
        вычисляет длину окружности
    """

    def __init__(self, radius : float):
        self.radius = radius

    def area(self) -> float:
        """Верни площадь круга."""

        return 3.14 * self.radius ** 2

    def perimeter(self) -> float:
        """Верни длину окружности."""

        return 2*3.14*self.radius

class Triangle(Shape):
    """Класс Triangle, наследующий класс Shape.

    Attributes
    ----------
    first_side : float
        первая сторона треугольника
    second_side : float
        вторая сторона треугольника
    third_side : float
        третья сторона треугольника

    Methods
    -------
    area() -> float
        вычисляет площадь треугольника по трём сторонам
    perimeter() -> float
        вычисляет периметр треугольника
    """

    def __init__(self, first_side : float, second_side : float, third_side : float):
        self.first_side = first_side
        self.second_side = second_side
        self.third_side = third_side

    def area(self) -> float:
        """Верни площадь треугольника."""

        p = round(self.perimeter() / 2, 2) # Вычисление полупериметра
        return math.sqrt(p * (p-self.first_side) * (p-self.second_side) * (p-self.third_side))

    def perimeter(self) -> float:
        """Верни периметр треугольника."""

        return self.first_side + self.second_side + self.third_side

if __name__ == "__main__":
    print("Примеры использования:")
    print("Rectangle(10, 20)"
          " -> создаёт объект типа Rectangle с атрибутами width=10 и height=20")
    print("rectangle1.area()"
          " -> возвращает площадь объекта rectangle1 типа Rectangle")
    print("rectangle1.perimeter()"
          " -> возвращает периметр объекта rectangle1 типа Rectangle")
    print()

shapes = [Rectangle(10, 20), Circle(4), Triangle(3,4,5)]

def print_shape_info(shapes_arg):
    """Выведи в консоль площадь и периметр всех фигур в shapes_arg."""

    for i in shapes_arg:
        print(f"Площадь равна {i.area()}. Периметр равен {i.perimeter()}")

print_shape_info(shapes)