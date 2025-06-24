class  Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello, " + name + "! You are " + age + " years old.")


x = 0
x = int(input("Enter a number: "))
if x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x is equal to 10")
elif x < 10:
    print("x is less than 10")


for i in range (1,11):
    print(i)

x = 10 
while x > 0:
    print(x)
    x -= 1 
    



def function_num(x = 1, y = 6):
    print(x+y)
function_num()  


Animals = [1, 10, 5,8]
print(max(Animals))  

