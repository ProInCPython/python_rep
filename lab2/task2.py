try:
    a, b = list(map(int, input().split()))
    y = a/b
except ZeroDivisionError:
    print("Ошибка деления на ноль!")
except ValueError:
    print("Неверный формат данных!")
else:
    print(y)
