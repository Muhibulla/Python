import csv 
import random
from random import randint
from collections import namedtuple


Color = namedtuple("Color", "red green blue alpha")

def random_color():
    red = randint(0, 255)
    blue = randint(0, 255)
    green = randint(0, 255)
    alpha = round(random.random(), 2)
    return Color(red, green, blue, alpha)

color = random_color()

print(color)

print(color.blue)

print(color.alpha)

print(color._fields)

# Creating a pen tool for paint

Pen = namedtuple("Pen", "width style beveled")

pen = Pen(2, "Solid", True)

if pen.width == 2 and pen.style == "Solid" and pen.beveled == True:
    print(f'Standard pen is selected')


with open("./jobs.csv", "r") as csv_file:
    reader = csv.reader(csv_file)
    Employee = namedtuple("Employee", next(reader), rename=True)
    for row in reader:
        employee = Employee(*row)
        print(employee.name, employee.job, employee.email)

 
#Add a New Field:
        '''Extend the `Person` named tuple to include a new field called `city`. Create instances with this new field'''
Person = namedtuple("Person", "name age gender city")

person1 = Person("Moiz", 2, "M", "Quetta")
print(person1)

#Namedtuple as Dictionary:
'''Convert a named tuple to a dictionary and vice versa.'''

person2 = person1._asdict()
print(person2)


print(Person.__name__.__doc__)

# Sorting Namedtuples:

people = [
    Person(name='Alice', age=30, gender='Female', city="karachi"),
    Person(name='Bob', age=25, gender='Male', city="kandhaar"),
    Person(name='Charlie', age=35, gender='Male', city="kabul")
]

people_sorted = sorted(people, key=lambda x: x.age)
people_sorted_city = sorted(people, key=lambda x: x.city)
print(people_sorted, people_sorted_city)











