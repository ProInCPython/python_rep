from typing import List

from lab3.task1 import Student
class Person:
    def __init__(self, name: str,age: int):
        self.name = name
        self.age = age

class Teacher(Person):
    def __init__(self, subject: str, students: List[Student], name, age):
        self.__subject = subject
        self.__students = students
        super().__init__(name, age)

    def get_subject(self):
        return self.__subject

    def get_students(self):
        return self.__students

    def add_student(self, student):
        self.__students.append(student)
    def remove_student(self, student_id):
        for i in self.__students:
            if i.get_student_id() == student_id:
                return i
        return "Студента с таким ID нет в списке!"

    def list_students(self):
        print(f"Студенты учителя с именем {self.name}")
        for i in range(len(self.__students)):
            print(self.__students[i].display_info())

teacher1 = Teacher("Реляционные базы данных", [], "Александр", 37)
teacher2 = Teacher("Дискретная математика", [], "Анастасия", 32)

student3 = Student("Елизавета", 3, [])
student4 = Student("Иван", 4, [])
student5 = Student("София", 5, [])

student3.add_grade(5)
student3.add_grade(6)
student3.add_grade(7)
student3.add_grade(10)

student4.add_grade(4)
student4.add_grade(3)
student4.add_grade(5)
student4.add_grade(7)

student5.add_grade(6)
student5.add_grade(7)
student5.add_grade(6)
student5.add_grade(9)

teacher1.add_student(student3)
teacher1.add_student(student4)

teacher2.add_student(student3)
teacher2.add_student(student4)
teacher2.add_student(student5)

teacher1.list_students()
print()
teacher2.list_students()