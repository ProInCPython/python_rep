from random import *
a = [randint(1,100) for i in range(20)]

print("Even numbers:", *list(filter(lambda x: x % 2 == 0, a))) # Фильтр тех чисел, которые делятся на два (=чётных)
print("Numbers that are divisible by 3:", *list(filter(lambda x: x % 3 == 0, a))) # Фильтр тех чисел, которые делятся на три
print("Arithmetical average:",sum(a) / len(a)) # Среднее арифметическое всех чисел в списке