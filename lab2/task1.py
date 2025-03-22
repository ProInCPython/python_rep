from random import *
f = open("data.txt", 'w')
for i in range(10):
    f.write(str(randint(1,100)) + '\n')

f.close()

f = open('data.txt', 'r')
a = list(map(int, [i.rstrip('\n') for i in f.readlines()]))

result = open('result.txt', 'w')

result.write(f"Сумма: {sum(a)}" + '\n')
result.write(f"Среднее: {sum(a) / len(a)}" + '\n')
result.write(f"Максимум: {max(a)}" + '\n')
result.write(f"Минимум: {min(a)}" + '\n')


result.close()
f.close()
