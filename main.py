# pandas = excel inside python
#DataFram = Data Table

import pandas as pd
data = pd.read_csv('big_students.csv')

data_cleaned = data.dropna()  # remove rows with null values
data_cleaned = data.drop_duplicates() # remove duplicate rows
print(data.isnull().sum()) # we know how many null values are in each column





# print(len(data)) to know how many rows are in the dataset
# print(data['age']) to know how the ages for each student
# print(data['age'].mean())  # Average age of students
# print(data['age'].max())   # Maximum age of students
# print(data['age'].min())   # Minimum age of students    
