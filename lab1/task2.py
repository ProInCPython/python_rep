n = int(input())
all_list = []
sq_list = []
[all_list.append(i) for i in range(1, n+1)] # для каждого числа от 1 до n (включительно) добавляем это число в список all_list с помощью команды append
[sq_list.append(j**2) for j in range(1, n+1)] # для каждого числа от 1 до n (включительно) добавляем квадрат этого числа в список sq_list с помощью команды append
print("List of numbers from 1 to n:", *all_list) # Выводим элементы первого списка через пробел
print("List of squares of numbers from 1 to n:", *sq_list) # Выводим элементы второго списка через пробел
print("Sum of all numbers from 1 to n:", sum(all_list))
