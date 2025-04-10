import csv
import student_utils
from datetime import datetime
f = open("students.csv", newline='')
reader = csv.reader(f)
data = [{"name":str(i[0]), "age":int(i[1]), "avg score":float(i[2])} for i in reader]
print([[i["name"] + " - " + str(i["age"])] for i in sorted(data,key=lambda x: (x["age"],x["name"]))])

report = open("report.txt", "a")
top_students = student_utils.get_top_students(data)
average_age = f"Average age: {student_utils.get_average_age(data)}"
filtered_students = f"Students with > 4.5 score: {student_utils.filter_by_grade(data, 4.5)}"
curr_date_and_time = str(datetime.now().year) + "/" + str(datetime.now().month) + "/" + str(datetime.now().day) + " " + str(datetime.now().hour) + ":" + str(datetime.now().minute) + ":" + str(datetime.now().second)
report.write(f"Time: {curr_date_and_time}\n")
report.write("Top students:\n")
for i,v in enumerate(top_students):
    report.write(f"\t{i+1}) {str(v[0])}\n")
report.write(average_age+"\n")
report.write(filtered_students+"\n\n")

report.close()
f.close()


