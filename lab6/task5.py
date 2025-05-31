import pandas as pd
import matplotlib.pyplot as plt

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
data_grouped = data.groupby(["Group"])["Score"].mean()
data_grouped.plot(kind="bar", x="Group", y="Score", xlabel="Group name", ylabel="Average score", title="Average score by groups", rot=0, colormap="gist_heat")

plt.legend()
plt.show()
