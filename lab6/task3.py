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


print("--------------Task 3--------------", '\n')

data.loc[5000] = ['David', 21, 'Mathematics', None]
data.loc[5001] = ['John', 19, None, None]
print(data.isna().sum())

data["Score"].fillna(data["Score"].mean(), inplace=True)

data.dropna(subset=['Group'], inplace=True)

print(data.tail(5))