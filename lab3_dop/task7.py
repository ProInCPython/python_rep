from typing import List
import random
from lab3.task1 import Student
from lab3.task2 import Teacher


class Assistant(Student, Teacher):
    """Класс Assistant, наследующий класс Student и Teacher.

        Attributes
        ----------
        name : str
            имя ассистента
        __student_id : int, private
            идентификатор ассистента
        __grades : List[int], private
            список всех оценок ассистента
        age : int
            возраст ассистента
        __subject : str, private
            предмет, который ведёт ассистент
        __students : List[Student], private
            список всех студентов ассистента

        Methods
        -------
        help_student(st_id)
            С вероятностью 50% ассистент может помочь студенту с указанным ID.
            В консоль выводится соответствующее сообщение.
        """
    def __init__(self, name: str, student_id: int, grades: List[int], subject: str, students: List[Student], age : int):
        Student.__init__(self, name, student_id, grades)
        Teacher.__init__(self, subject, students, name, age)

    def help_student(self, st_id : int):
        """Выведи в консоль сообщение о результате попытки помощи студенту с ID, равным st_id

        Parameters
        ----------
        st_id : int
            ID студента, которому нужно помочь
        Если ID студента не был указан, метод возвращает сообщение "Не указан ID студента."
        """

        if st_id == 0:
            print(f"Не указан ID студента.")
        else:
            if random.randint(1,100) > 50:
                print(f"Я успешно помог студенту со следующим ID: {st_id}")
            else:
                print(f"Я не смог помочь студенту со следующим ID: {st_id}. Извините.")

if __name__ == "__main__":
    print("Примеры использования:")
    print("Assistant(name, student_id, grades, subject"
          "students, age)) -> создаёт объект типа Assistant с атрибутами name, student_id, grades, subject, students, age")
    print("assistant1.add_grade(5) -> добавляет в список оценок оценку 5")
    print("assistant1.get_average() -> возвращает среднюю оценку ассистента")
    print("assistant1.list_students() -> выводит в консоль список студентов объекта assistant1 типа Assistant")
    print("assistant1.help_student(4) -> ассистент с вероятностью 50% поможет студенту с ID 4.")
    print()

# student1 = Student("Вася", 1,[])
#
# student1.add_grade(5)
# student1.add_grade(6)
# student1.add_grade(7)
# student1.add_grade(8)
# student1.add_grade(8)
# print(student1.get_average())
# assistant = Assistant("John", 10,[], "Maths", [], 35)
# assistant.add_grade(5)
# assistant.add_student(student1)
#
# assistant.list_students()
# assistant.display_info()
# assistant.help_student(1)







