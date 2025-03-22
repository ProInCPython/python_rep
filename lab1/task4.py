from random import *
a = [randint(1,100) for i in range(10)]

print(*a)
print(f"MAX={max(a)}, MIN={min(a)}")
print(f"SUM={sum(a)}")
print("List:", *sorted(a))