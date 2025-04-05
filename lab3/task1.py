from typing import List


class Student:
    def __init__(self, name: str, student_id: int, grades: List[int]):
        self.__name = name
        self.__student_id = student_id
        self.__grades = grades

    def get_name(self):
        return self.__name

    def get_student_id(self):
        return self.__student_id

    def get_grades(self):
        return self.__grades

    def add_grade(self, grade):
        if 0 <= grade <= 10:
            self.__grades.append(grade)
        else:
            return "Оценка не попадает в границы(0-10)!"
    def get_average(self):
        return f"Средняя оценка: {round(sum(self.__grades) / len(self.__grades), 3)}"
    def display_info(self):
        return f"Имя студента: {self.__name}. \nID студента: {self.__student_id}. \nОценки студента: " + (" ".join(list(map(str, self.__grades))))

student1 = Student("Вася", 1,[])

student1.add_grade(5)
student1.add_grade(6)
student1.add_grade(7)
student1.add_grade(8)
student1.add_grade(8)
print(student1.add_grade(-2))
print(student1.get_average())
print(student1.display_info())

student2 = Student("Сергей", 2,[])
student2.add_grade(10)
student2.add_grade(9)
student2.add_grade(9)
student2.add_grade(9)
student2.add_grade(10)
print(student2.get_average())
print(student2.display_info())