import pandas as pd

data = pd.read_csv('big_students.csv')
print(data.head())


# print(len(data)) to know how many rows are in the dataset
# print(data['age']) to know how the ages for each student
# print(data['age'].mean())  # Average age of students
# print(data['age'].max())   # Maximum age of students
# print(data['age'].min())   # Minimum age of students    