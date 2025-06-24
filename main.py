
import csv 
with open('big_students.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)      