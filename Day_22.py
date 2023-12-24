import random

print(random.random())

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sort_lst = sorted(lst, key= lambda x: random.random())
print(sort_lst)

fnat = ['1', '3', '3']
def conver_add(data):
    return sum(int(i) for i in data)

print(conver_add(fnat))


def check_dup(input_data):
    for i in input_data:
        if input_data.count(i) > 1:
            return i
        else:
            return 'No duplicate.' 

students = ['moiz', 'muhib', 'khan', 'moiz']

print(check_dup(students))


l = [2, 3, 4, 5, 6, 7]
list_comp = [value for value in l if value % 2 == 0]
print(list_comp)

range = range(10)
list_comp = [x**2 for x in range if x**2 < 25]
print(list_comp)


numbers = [1, 2, 3, 4, 5]
number = []

for values in numbers:
    number.append(values**2)

print(number)

def square(number):
    return number**2

square_list = list(map(square, numbers)) 
print(sort_lst)

str_nums = ["4", "8", "6", "5", "3", "2", "8", "9", "2", "5"]

int_nums = list(map(int, str_nums))
print(int_nums)


str_nums = ["4", "8", "6", "5", "3", "2", "8", "9", "2", "5"]

int_nums = sum(map(int, str_nums))
print(int_nums)



str_nums = ["4", "8", "6", "5", "3", "2", "8", "9", "2", "5"]

int_number = list(map(int, str_nums))
print(int_number)


numbers = [-2, -1, 0, 1, 2]

number = list(map(abs, numbers))
print(number)

number = list(map(float, numbers))
print(number)

'''You can use any built-in function with map(), provided that the function takes an argument and returns a value.'''

first_l = [1, 3, 5]
second_l = [2, 4, 8, 16]

result = list(map(pow, first_l, second_l))
print(result)


string_it = ["processing", "strings", "with", "map"]
result = list(map(str.capitalize, string_it))
print(result)

string_it = ["processing", "strings", "with", "map"]
result = list(map(str.casefold, string_it))
print(result)

string_it = ["processing", "strings", "with", "map"]
result = list(map(str.title, string_it))
print(result)

'''https://realpython.com/python-map-function/'''



class Car:
    def __init__(self, name, modle, price):
        self.name = name
        self.modle = modle
        self.price  = price
        self.is_running = False

    def is_start(self):
        self.is_running = True
        print(f"{self.name} {self.modle} is start.")

    def is_stopped(self):
        self.is_running = False
        print(f"{self.name} {self.modle} is stopped.")

my_car = Car("toyota", 2016, 200)
my_car.is_start()
my_car.is_stopped()







class Laptop:
    def __init__(self, name, modle):
        self.name = name
        self.modle = modle
        is_Onn = False

    def turn_on(self):
        self.is_Onn = True
        print(f"{self.name} having modle {self.modle} is On.")

    def turn_off(self):
        self.is_Onn = False
        print(f"{self.name} having modle {self.modle} is Off.")

my_laptop = Laptop("Asusvivobook", 2022)
my_laptop2 = Laptop("Dell", 2019) 

my_laptop.turn_on()
my_laptop2.turn_off()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def validate_age(self):
        if not 0 <= self.age <= 120:
            raise ValueError(f"{self.age} must be between 0 to 120 years.")
        
    def get_age(self):
        return  self.age
    
    def set_age(self, new_age):
        self.age = new_age
        self.validate_age()

per1 = Person("muhib", 18)
print("Current age", per1.get_age())

import math

def is_positive(numb):
    return numb > 0

def sanitize_sqrt(numbers):
    cleaned_iter = list(map(math.sqrt, filter(is_positive, numbers)))
    return cleaned_iter

test_sqrt = [-16, 2, 55, 7, -5]
print(sanitize_sqrt(test_sqrt))
        

        


numbers = [1, 2, 4, 6, 8, 3, 99, 34, 45, 6, 7]
sort = sorted(numbers, reverse=True)
print(sort) # the out put is new sorted list.


#help(sorted)

tuple_numbers = (1, 2, 4, 6, 8, 3, 99, 34, 45, 6, 7)
dictionary_numbers = {1, 2, 4, 6, 8, 3, 99, 34, 45, 6, 7}

tuple_sort = sorted(tuple_numbers)
dictionary_sorted = sorted(dictionary_numbers)
print(tuple_sort)
print(dictionary_sorted)
ordered_tuple = tuple(tuple_sort)
print(ordered_tuple)


str_value = 'I love python.'
print(sorted(str_value))

# sorted() on string will treat each string a list and iterate through it.

similar_values = [False, 0, 1, 'A' == 'B', 1 <= 0]

print(sorted(similar_values))

false_values = [False, 0, 0, 1 == 2, 0, False, False]

print(sorted(false_values))

names = ['Harry', 'Suzy', 'Al', 'Mark']

print(sorted(names))

different_lengths = ['hhhh', 'hh', 'hhhhh','h']
print(sorted(different_lengths))


# sorted() With a key Argument
different_lengths = ['hhhh', 'hh', 'hhhhh','h']

print(sorted(different_lengths, key=len))
print(sorted(names, key=len))

names_with_case = ['harry', 'Suzy', 'al', 'Mark']
print(sorted(names_with_case, key=len))

my_list = [(1, 5), (3, 2), (2, 8), (4, 1)]

print(sorted(my_list, key=lambda x: x[1]))

'''
my_list = [(1, ), (3, 2), (2, ), (4, 1)]

print(sorted(my_list, key=lambda x: x[1]))

To sort this list based on the second element of each tuple, you can use the key parameter of the sorted() function and pass a lambda function that returns the second element of each tuple. However, since some tuples in your list do not have a second element, you need to modify the lambda function to handle this case. One way to do this is to use the get() method of the tuple object to return a default value of None if the second element does not exist

'''
import functools

my_list = [(1, ), (3, 2), (2, ), (4, 1)]

print(sorted(my_list, key=lambda x: (x[1][0] if len(x) > 0 else x[1]) if len(x) > 1 else None))





















































        