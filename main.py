# pandas = excel inside python
#DataFrame = Data Table
import pandas as pd #importing pandas library
import matplotlib.pyplot as plt # matplotlib is a plotting library

data = pd.read_csv('big_students.csv')

data_cleaned = data.dropna()  # remove rows with null values
data_cleaned = data.drop_duplicates() # remove duplicate rows
print(data.isnull().sum()) # we know how many null values are in each column

print(data.describe())  # gives us a statistical summary of the dataset

# Plot the distribution of age
plt.hist(data['age'], bins=10, color='blue', edgecolor='black') # Create a histogram of the 'age' column
plt.title('Distribution of age') #Title of the plot
plt.xlabel('age') #X-axis label
plt.ylabel('Number of Students') #Y-axis label
plt.show() #show the plot

plt.hist(data['age'], bins=10, color='purple', edgecolor='red')
plt.title('Distribtion of age')
plt.xlabel('age')
plt.ylabel('Number of Students')


# print(len(data)) to know how many rows are in the dataset
# print(data['age']) to know how the ages for each student
# print(data['age'].mean())  # Average age of students
# print(data['age'].max())   # Maximum age of students
# print(data['age'].min())   # Minimum age of students    
