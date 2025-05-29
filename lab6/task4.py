import pandas as pd

def is_passed(score):
    if score >= 60:
        return 1
    else:
        return 0

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

print("--------------Task 4--------------", '\n')

print(data.groupby(["Group"]).agg({'Score' : 'mean', 'Age' : 'median'}), '\n')


data["Passed"] = data["Score"].apply(func=is_passed)


print(data.head(10))