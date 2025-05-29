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


print("--------------Task 2--------------", '\n')

print(data[data["Score"] > 80])
print(data[data["Score"] > 80].sort_values('Score', ascending=False))

print("Самый старший студент:")
print(data[data["Age"] == data["Age"].max()].sort_values('Name', ascending=True).head(1), '\n')
print("Самый младший студент:")
print(data[data["Age"] == data["Age"].min()].sort_values('Name', ascending=True).head(1), '\n')