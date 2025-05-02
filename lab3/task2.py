from typing import List

from lab3.task1 import Student
class Person:
    """Класс Person.

    Attributes
    ----------
    name : str
        имя человека
    age : int
        возраст человека
    """

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

class Teacher(Person):
    """Класс Teacher, наследующий класс Person.

    Attributes
    ----------
    name : str, private
        имя преподавателя
    age : int, private
        возраст преподавателя
    __subject : str, private
        предмет, который ведёт преподаватель
    __students : List[Student], private
        список всех студентов преподавателя

    Methods
    -------
    get_subject() -> str
        Возвращает предмет, который ведёт преподаватель
    get_students() -> List[Student]
        Возвращает список всех студентов преподавателя
    add_student(student)
        Добавляет студента в students
    remove_student(student_id)
        Удаляет студента с заданным идентификатором из students
    list_students()
        Выводит в консоль список всех студентов преподавателя в формате:
        "Студенты учителя с именем *имя преподавателя*
        *список всех студентов учителя, каждый студент выводится в формате Student.display_info()*
        """

    def __init__(self, subject: str, students: List[Student], name : str, age : int):
        self.__subject = subject
        self.__students = students
        super().__init__(name, age)

    def get_subject(self) -> str:
        """Верни предмет, который ведёт преподаватель."""

        return self.__subject

    def get_students(self) -> List[Student]:
        """Верни список всех студентов преподавателя."""

        return self.__students

    def add_student(self, student : Student = None):
        """Добавь студента в students.

        Parameters
        ----------
        student : Student
            студент, которого нужно добавить в students

        Если студент не был указан, метод возвращает сообщение "Не указан студент."
        """

        if student is None:
            return "Не указан студент."
        else:
            self.__students.append(student)

    def remove_student(self, student_id : int = 0):
        """Добавь студента в students.

        Parameters
        ----------
        student_id : int
            идентификатор студента, которого нужно удалить из students
            если студента с заданным идентификатором нет в students,
            метод возвращает сообщение "Студента с таким ID нет в списке!"

        Если student_id не указан или меньше либо равен 0,
        метод возвращает сообщение "ID студента меньше либо равен 0."
        """

        if student_id <= 0:
            return "ID студента меньше либо равен 0."
        for i in self.__students:
            if i.get_student_id() == student_id:
                return i
        return "Студента с таким ID нет в списке!"

    def list_students(self):
        """Выведи в консоль список всех студентов преподавателя."""

        print(f"Студенты учителя с именем {self.name}:")
        for i in range(len(self.__students)):
            print(self.__students[i].display_info())

if __name__ == "__main__":
    print("Примеры использования:")
    print("Teacher(subject, students, name, age) -> создаёт объект типа Teacher с атрибутами subject, students, name, age")
    print("teacher1.add_student(student3) -> добавляет в список студентов объекта teacher1 типа Teacher объект student3 типа Student")
    print("teacher1.list_students() -> выводит в консоль список студентов объекта teacher1 типа Teacher")
    print()
# teacher1 = Teacher("Реляционные базы данных", [], "Александр", 37)
# teacher2 = Teacher("Дискретная математика", [], "Анастасия", 32)
#
# student3 = Student("Елизавета", 3, [])
# student4 = Student("Иван", 4, [])
# student5 = Student("София", 5, [])
#
# student3.add_grade(5)
# student3.add_grade(6)
# student3.add_grade(7)
# student3.add_grade(10)
#
# student4.add_grade(4)
# student4.add_grade(3)
# student4.add_grade(5)
# student4.add_grade(7)
#
# student5.add_grade(6)
# student5.add_grade(7)
# student5.add_grade(6)
# student5.add_grade(9)
#
# teacher1.add_student(student3)
# teacher1.add_student(student4)
#
# teacher2.add_student(student3)
# teacher2.add_student(student4)
# teacher2.add_student(student5)
#
# teacher1.list_students()
# print()
# teacher2.list_students()
