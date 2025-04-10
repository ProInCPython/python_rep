import re
f = open("server_logs.txt", "r")
s = []
for i in f:
    s.append(i.strip()) # Добавляем в список s строки из файла, удаляя знак переноса строки

logs = re.findall("(\d{4}\-\d{2}\-\d{2})\ (\d{2}\:\d{2}\:\d{2})\ (\d+\.\d+\.\d+\.\d+)\ (POST|GET|PUT|OPTIONS|HEAD|DELETE|PATCH)\ (https?:\/\/?[\da-z\.-]+\.[a-z\.]{2,6}[\/\w\.-]*)*\/?\ (\d{3})\ (\d+\.?\d*)\ (B|KB|MB|GB|TB)", " ".join(s))
success = sum([1 if i[5] == "200" else 0 for i in logs]) # Если код равен 200, тогда добавляем в список 1. В противном случае добавляем 0. Вычисляя сумму элементов в списке, как раз получаем кол-во записей с кодом 200.
total_size = 0
unique_ip = set()
for i in logs: # Считаем общий объём
    unique_ip.add(i[2]) # Добавляем во множество IP адреса, так как там сохраняются только уникальные элементы.
    if i[7] == "KB":
        total_size += round(float(i[6]) / 1024, 2)
    elif i[7] == "MB":
        total_size += float(i[6])
    elif i[7] == "GB":
        total_size += float(i[6]) * 1024
    elif i[7] == "TB":
        total_size += float(i[6]) * 1024 * 1024

for j in sorted(logs, key=lambda x: (x[0], x[1]), reverse=True)[:10]: # Красиво выводим записи в логе
    print(f"Дата: {j[0]}")
    print(f"Время: {j[1]}")
    print(f"IP: {j[2]}")
    print(f"Метод: {j[3]}")
    print(f"URL: {j[4]}")
    print(f"Статус: {j[5]}")
    print(f"Размер: {j[6]} {j[7]}")
    print()

f2 = open("log_analysis.txt", "w")
# Добавляем все полученные данные в файл
f2.write(f"Successful requests: {success}\n")
f2.write(f"Total size: {round(total_size, 1)} MB\n")
f2.write(f"Unique IP: {len(unique_ip)}\n")

f.close()
f2.close()