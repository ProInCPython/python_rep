from lab3.task1 import Student
from lab3.task2 import Teacher

from datetime import datetime


class Assistant(Student, Teacher):
    def __init__(self):
        pass
        #super().__init__()

    def help_student(self):
        pass

time = datetime.now()

for i in range(1000):
    print(i)

print(type(datetime.now() - time))

