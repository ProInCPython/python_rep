import random
a = [i for i in range(1, 21)]
random.shuffle(a)

print("Initital list:", *a)

even_only = list(filter(lambda x: x % 2 == 0, a))
print("Even numbers only:", *even_only)

added_ten = list(map(lambda x: x+10, a))
print("Every element increased by 10:", *added_ten)

sorted_list = sorted(a, key=lambda x: abs(x), reverse=True)
print("List sorted in descending order:", *sorted_list)