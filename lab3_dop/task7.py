from lab3.task1 import Student
from lab3.task2 import Teacher


class Assistant(Student, Teacher):
    def __init__(self):
        pass
        #super().__init__()

    def help_student(self):
        pass

a = Assistant()
