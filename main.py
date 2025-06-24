# pandas = excel inside python
#DataFrame = Data Table
import pandas as pd #importing pandas library
import matplotlib.pyplot as plt # matplotlib is a plotting library
from sklearn.linear_model import LinearRegression #importing linear regression model from sklearn


data = pd.read_csv('big_students.csv') # reading the csv file into a pandas DataFrame

x = data[['age']] # selecting the 'age' column as feature variable
y =data[['score']] # selecting the 'score' column as target variable

model = LinearRegression() # creating an instance of the LinearRegression model

model.fit(x, y) # fitting the model to the data


print("Coefficient:", model.coef_[0])   # printing the coefficient of the model
print("Intercept:", model.intercept_) # printing the intercept of the model

# Plot data and the learned regression line


plt.scatter(x,y , color="blue", label ='Actual data') # scatter plot of the actual data points

plt.plot(x, model.predict(x), color='red', label='Regression line') # plot the regression line

plt.title('Age vs Grade') # title of the plot
plt.xlabel('Age') # x-axis label
plt.ylabel('Grade') # y-axis label
plt.legend() # show the legend
plt.show() # display the plot

new_age = [[22]] # new age value for prediction
predicted_grade = model.predict(new_age) # predicting the grade for the new age value

print(f"Expected grade for student aged 22: {predicted_grade[0]}") # Uncomment the following lines to perform data cleaning and exploration



# data_cleaned = data.dropna()  # remove rows with null values
# data_cleaned = data.drop_duplicates() # remove duplicate rows
# print(data.isnull().sum()) # we know how many null values are in each column

# print(data.describe())  # gives us a statistical summary of the dataset

# # Plot the distribution of age
# plt.hist(data['age'], bins=10, color='blue', edgecolor='black') # Create a histogram of the 'age' column
# plt.title('Distribution of age') #Title of the plot
# plt.xlabel('age') #X-axis label
# plt.ylabel('Number of Students') #Y-axis label
# plt.show() #show the plot

# plt.hist(data['age'], bins=10, color='purple', edgecolor='red')
# plt.title('Distribtion of age')
# plt.xlabel('age')
# plt.ylabel('Number of Students')


# print(len(data)) to know how many rows are in the dataset
# print(data['age']) to know how the ages for each student
# print(data['age'].mean())  # Average age of students
# print(data['age'].max())   # Maximum age of students
# print(data['age'].min())   # Minimum age of students    
