from typing import List


class Student:
    """Класс Student.

    Attributes
    ----------
    __name : str, private
        имя студента
    __student_id : int, private
        идентификатор студента
    __grades : List[int], private
        список всех оценок студента

    Methods
    -------
    get_name() -> str
        Возвращает имя студента
    get_student_id() -> int
        Возвращает идентификатор студента
    get_grades() -> List[int]
        Возвращает список оценок студента
    add_grade(grade)
        Добавляет оценку в grades.
        При оценке, меньшей 0 или большей 10, возвращает сообщение "Оценка не попадает в границы(0-10)!"
    get_average() -> str
        Возвращает среднюю оценку студента в формате "Средняя оценка: *средняя оценка*"
    display_info() -> str
        Возвращает информацию о студенте в формате:
        "Имя студента: *имя студента*
        ID студента: *идентификатор студента*
        Оценки студента: *список оценок студента через пробел*"
    """

    def __init__(self, name: str, student_id: int, grades: List[int]):
        self.__name = name
        self.__student_id = student_id
        self.__grades = grades

    def __str__(self): # Задание 5
        return f"Имя студента: {self.__name}. ID студента: {self.__student_id}. Оценки студента: " + (" ".join(list(map(str, self.__grades))))

    def __eq__(self, other): # Задание 5
        return self.__student_id == other.__student_id

    def __len__(self): # Задание 5
        return len(self.__grades)

    def get_name(self) -> str:
        """Верни имя студента."""

        return self.__name

    def get_student_id(self) -> int:
        """Верни идентификатор студента."""

        return self.__student_id

    def get_grades(self) -> List[int]:
        """Верни список оценок студента."""

        return self.__grades

    def add_grade(self, grade : int):
        """Добавь оценку в список оценок.

        Parameters
        ----------
        grade : int
            оценка, которую надо добавить в список оценок
            должна быть в пределе от 0 до 10 включительно
        """

        if 0 <= grade <= 10:
            self.__grades.append(grade)
        else:
            return "Оценка не попадает в границы(0-10)!"

    def get_average(self) -> str:
        """Верни среднюю оценку студента."""

        return f"Средняя оценка: {round(sum(self.__grades) / len(self.__grades), 3)}"

    def display_info(self) -> str:
        """Верни информацию о студенте."""

        return f"Имя студента: {self.__name}. \nID студента: {self.__student_id}. \nОценки студента: " + (" ".join(list(map(str, self.__grades))))

if __name__ == "__main__":
    print("Примеры использования:")
    print("Student(name, student_id, grades) -> создаёт объект типа Student с атрибутами name, student_id, grades")
    print("student1.add_grade(5) -> добавляет в список оценок оценку 5")
    print("student1.get_average() -> возвращает среднюю оценку студента")
    print("student1.display_info() -> возвращает информацию о студенте")
    print()

# student1 = Student("Вася", 1,[])

# student1.add_grade(5)
# student1.add_grade(6)
# student1.add_grade(7)
# student1.add_grade(8)
# student1.add_grade(8)
# print(student1.add_grade(-2))
# print(student1.get_average())
# print(str(student1)) # -> Имя студента: Вася. ID студента: 1. Оценки студента: 5 6 7 8 8
# print(len(student1)) # -> 5
#
# student2 = Student("Сергей", 1,[])
# student2.add_grade(10)
# student2.add_grade(9)
# student2.add_grade(9)
# student2.add_grade(9)
# student2.add_grade(10)
# print(student2.get_average())
# print(student2.display_info())
#
# print(student1.__eq__(student2)) # -> True