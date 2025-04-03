import re
f = open("text2.txt", "r")
def converter(date): # Функция для конвертации одного формата даты в другой.
    s = date[6:] + "-" + date[3:5] + "-" + date[:2]
    return s


data = f.readline()
dates = re.findall("\d{2}\.\d{2}\.\d{4}", data)
correct_dates = list(filter(lambda x: x != 0, [i if (1 <= int(i[0:2]) <= 31) and (1 <= int(i[3:5]) <= 12) else 0 for i in dates])) # Оставляем только те даты, у которых число от 1 до 31, а номер месяца - от 1 до 12

converted_dates = list(map(converter, correct_dates)) # Применяем к каждому элементу списка correct_dates функцию converter
sorted_dates = sorted(converted_dates, key=lambda x: int(x[0:4]))
for i in sorted_dates:
    print(i, end="\n")

d_f = open("dates.txt", "w")
d_f.write("\n".join(sorted_dates))

d_f.close()
f.close()