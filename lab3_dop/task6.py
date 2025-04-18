class Temperature:
    """Класс Temperature

        Класс используется для хранения температуры
        в градусах Цельсия и в градусах Фаренгейта

        Attributes
        ----------
        __celsius : float, private
            температура в градусах Цельсия
        fahrenheit : float, dynamic
            температура в градусах Фаренгейта - динамическое свойство


        Methods
        -------
        @property
        celsius() -> float
            Метод с декоратором @property,
            позволяет получить значение атрибута __celsius
        @celsius.setter
        celsius(celsius)
            Сеттер для атрибута __celsius
        @celsius.deleter
        celsius()
            Сбрасывает значение атрибута __celsius в 0
        @property
        fahrenheit() -> float
            Геттер для динамического свойства fahrenheit.
            Возвращает сообщение в формате
            "Температура в градусах Фаренгейта равна *температура в градусах Фаренгейта*"
        @fahrenheit.setter
            Сеттер для динамического свойства fahrenheit.
            При этом температура конвертируется в градусы Цельсия
            и сохраняется в атрибуте __celsius
        """

    def __init__(self, celsius : float = 0):
        self.__celsius = celsius

    @property
    def celsius(self):
        """Верни температуру в градусах Цельсия"""

        return f"Температура в градусах Цельсия равна {self.__celsius}"

    @celsius.setter
    def celsius(self, celsius : float):
        """Задай новое значение температуры в градусах Цельсия

        Parameters
        ----------
        celsius : float
            новое значение температуры в градусах Цельсия

        Если celsius имеет некорректный тип, значение атрибута __celsius не меняется.
        В консоль печатается сообщение "Некорректный тип входных данных"
        """

        try:
            self.__celsius = celsius
        except TypeError:
            print("Некорректный тип входных данных")

    @celsius.deleter
    def celsius(self):
        """Сбрось значение атрибута __celsius в 0"""

        self.__celsius = 0

    @property
    def fahrenheit(self):
        """Верни температуру в градусах Фаренгейта"""

        return f"Температура в градусах Фаренгейта равна {(self.__celsius * 9 / 5) + 32}"

    @fahrenheit.setter
    def fahrenheit(self, value : float):
        """Задай новое значение температуры в градусах Фаренгейта

        Parameters
        ----------
        value : float
            новое значение температуры в градусах Фаренгейта

        Конвертирует value в градусы Цельсия
        и присваивает это значение атрибуту __celsius

        Если value имеет некорректный тип, значение атрибута __celsius не меняется.
        В консоль печатается сообщение "Некорректный тип входных данных"
        """

        try:
            self.__celsius = (value - 32) * 5 / 9
        except TypeError:
            print("Некорректный тип входных данных")

# t = Temperature()
#
# t.celsius = -20
# print(t.fahrenheit)
# print(t.celsius)
#
# t.fahrenheit = "str"
# print(t.fahrenheit)
# print(t.celsius)