a, b, c = list(map(int, input("Введите 3 числа через пробел: ").split())) # Ввод с клавиатуры

print("Max element:", max(a,b,c))
print("Min element:", min(a,b,c))
print("All three numbers are the same:", a == b == c)