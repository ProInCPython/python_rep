import pandas as pd

data = pd.read_csv("students.csv")
data.drop(columns=['Student_ID','Last_Name', 'Email', 'Gender', 'Attendance (%)',
                   'Midterm_Score', 'Final_Score', 'Assignments_Avg',
                   'Quizzes_Avg', 'Participation_Score', 'Projects_Score',
                   'Grade', 'Study_Hours_per_Week', 'Extracurricular_Activities',
                   'Internet_Access_at_Home', 'Parent_Education_Level',
                   'Family_Income_Level', 'Stress_Level (1-10)',
                   'Sleep_Hours_per_Night'], inplace=True)
data.rename(columns={'First_Name' : 'Name',
                     'Department' : 'Group', 'Total_Score' : 'Score'}, inplace=True)

print("--------------Task 1--------------", '\n')
print(data.head(5), '\n')
print(data.info(), '\n')
print(data.describe(), '\n')

print("Средний балл студентов:", round(data["Score"].mean(), 2), '\n')
print(f"Кол-во студентов в каждой группе:\n{data['Group'].value_counts()}", '\n')
