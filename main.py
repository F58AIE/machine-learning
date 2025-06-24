# # # # first_name = "ahmed"
# # # # last_name = "Mohd"
# # # # print("My name is: " +first_name + " " + last_name)

# # # # # string "I love Python"
# # # # wht = "I love Python" 
# # # # print(wht);
# # # # # integer 201
# # # # ints = 201
# # # # print(int)
# # # # # float 99.9
# # # # floats = 99.9
# # # # print(float)
# # # # # boolean true or false
# # # # bools = True
# # # # print(bool)


# # # # name = "F58AIE"
# # # # age = 30
# # # # score = 99.9
# # # # engineer = True
# # # # print("My name is:" + name  + " and my age is: " + str(age) + " and my score is: " + str(score) + " and I am an engineer: " + str(engineer))


# # # # # * / + - 
# # # # num1 = 12
# # # # num2 = 93
# # # # print(num1 + num2)
# # # # print(num1 * num2)
# # # # print(num1 / num2)
# # # # print(num1 - num2) 
# # # # print(num1 ** num2)  # Exponentiation operation
# # # # num5 = 15
# # # # num4 = "432"
# # # # print(num5 + int(num4))  # Convert string to integer before addition
# # # # print(num5 * int(num4))  # Convert string to integer before multiplication
# # # # print(num5 / int(num4))  # Convert string to integer before division
# # # # print(num5 - int(num4))  # Convert string to integer before subtraction 
# # # # print(num5 ** int(num4))  # Convert string to integer before exponentiation

# # # # name = input ("What is your name? ")
# # # # age = input("what is your age? ")
# # # # print("Your name is: " + name + " and your age is: " + age)


# # # # num1 = input ("Enter first number: ")
# # # # num2 = input("Enter second number: ")
# # # # print(int(num1) + int(num2)) # Convert


# # # # for x in range(0, 101 , 2):
# # # #     print("Hello World " + str(x))
# # # # # for x in range from 0 to 100 because the range function starts from 0 by default
# # # # # The step value of 2 means it will print every second number (even numbers only).

# # # # name = "Casey Harper"
# # # # for x in name:
# # # #     print(x)
# # # # # This will print each character in the string "name" on a new line.


# # # # names = ["Casey Harper", "John Doe", "Jane Smith"]
# # # # for name in names:
# # # #     print(name)
# # # # # This will print each name in the list "names" on a new line.

# # # # cars = ["Toyota", "Honda", "Ford"]
# # # # adjectives = ["fast", "reliable", "affordable"]
# # # # for car in cars:
# # # #     for adjective in adjectives:
# # # #         print(car + " is " + adjective)
# # # # # This will print each car with each adjective, resulting in combinations like "Toyota is fast",
# # # # # "Toyota is reliable", etc. It will iterate through each car and for each car,
# # # # # it will iterate through all the adjectives, printing all combinations.    



# # # while True:
# # #     name = input("Enter your name (or type 'exit' to quit): ")
# # #     if name.lower() == 'exit':
# # #         print("Exiting the program.")
# # #         break
# # #     else:
# # #         print("Hello, " + name + "!")
# # # # This code will keep asking for the user's name until they type 'exit'.
# # # # It uses a while loop to continuously prompt for input and checks if the input is 'exit'.
# # # # If it is, the program will print a message and break out of the loop, effectively ending the program.
# # # # If the input is anything else, it will greet the user with their name.
# # # # The `lower()` method is used to make the check case-insensitive, so 'Exit', 'EXIT', etc., will also work to exit the loop. 

# # # while True: 
# # #     name = input("Enter your name")
# # #     if name:
# # #         print("Hello, " + name + "!")
# # #         break
# # #     else:
# # #         print("You didn't enter a name. Please try again.") 
# # #         continue
# # # # This code will keep asking for the user's name until they enter a non-empty string.
# # # # It uses a while loop to continuously prompt for input and checks if the input is not empty.
# # # # If the input is not empty, it will greet the user with their name.


# # # number = input("Enter a number: ")
# # # number = int(number)  # Convert the input to an integer
# # # x = 0
# # # while x < 11:
# # #     x += 1
# # #     if x  == number:
# # #         continue
# # #     print(x)


# # name = input("Enter your name: ")
# # x = "Ali"
# # if name == x:
# #     print("Hello, " + name + "!")
# # else:
# #     print("You are not " + x + ", you are " + name + "!")




# # and
# score = input("Enter your score: ")
# score = int(score)  # Convert the input to an integer
# absence = input("Enter your absence: ")
# absence = int(absence)  # Convert the input to an integer
# if score >= 90 and absence <= 0 or score >= 95 and absence <= 1:
#     print("You excelled in the exam!")
# elif score >= 80 and absence <= 2 or score >= 85 and absence <= 1:
#     print("You are good!")
# elif score >= 70 and absence <= 4 or score >= 75 and absence <= 3: 
#     print("You are average!")
# else:
#     print("You need to work harder!")   

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
        
person_john = Person("John", 30)
person_john.display_info()
