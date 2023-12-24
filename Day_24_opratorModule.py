


''' The `operator` module in Python provides a set of efficient functions corresponding to the intrinsic operators of Python ¹. These functions are useful when we need to perform operations on objects, and they are equivalent to the intrinsic operators of Python. For example, `operator.add(x, y)` is equivalent to the expression `x+y` ¹. 

The functions in the `operator` module fall into categories that perform object comparisons, logical operations, mathematical operations, and sequence operations ¹. The object comparison functions are useful for all objects, and are named after the rich comparison operators they support ¹. The logical operations are also generally applicable to all objects, and support truth tests, identity tests, and boolean operations ¹. The mathematical and bitwise operations are the most numerous ¹.

Here is an example of how to use the `operator` module to perform addition on two numbers:

```python
import operator

a = 5
b = 10

addition = operator.add(a, b)
print(addition) # Output: 15
```

I hope this helps! Let me know if you have any other questions..

Source

(1) Working With the Python operator Module – Real Python. https://realpython.com/python-operator-module/.
(2) en.wikipedia.org. https://en.wikipedia.org/wiki/Python_(programming_language).'''


import operator

a = operator.add(5, 3)

b = operator.__add__(5, 3)

print(a)
print(b)

print(operator.truediv(5, 2))
print(operator.ge(5, 2))
print(operator.is_("X", "Y"))
print(operator.not_(5 < 3))


def perform_opration(oprator_str, oprator1, oprator2):
    if oprator_str == "+":
        return oprator1 + oprator2
    elif oprator_str == "-":
        return oprator1 - oprator2
    elif oprator_str == "*":
        return oprator1 * oprator2
    elif oprator_str == "/":
        return oprator1 / oprator2
    else:
        return "Invalid opration"

number1 = 10
number2 = 5
calculation = ["+", "-", "*", "/"]

for opration_str in calculation:
    print(perform_opration(opration_str, number1, number2))



def perform_opration(oprator_function, opartor1, oprator2):
    return oprator_function(opartor1, oprator2)

from operator import add, sub, mul, truediv

number1 = 20
number2 = 15

calculation = [ add, sub, mul, truediv]

for opration_str in calculation:
    print(perform_opration(opration_str, number1, number2))

'''Remember, the name of a function is actually a reference to its code. Using the () syntax calls the function.'''



'''oprators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}

import pickle

with open("operators.pkl", mode="wb") as f:
    pickle.dump(oprators, f)

def perform_opration(operator_function, number1, number2):
    return operator[operator_function](number1, number2)

print(perform_opration("-", 5, 10))'''


import operator
import pickle

operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}

with open("operators.pkl", mode="wb") as f:
    pickle.dump(operators, f)

def perform_operation(operator_function, number1, number2):
    return operators[operator_function](number1, number2)

print(perform_operation("-", 5, 10))


'''Selecting Values From Multidimensional Collections With itemgetter()'''
#To begin with, create a list of dictionaries:

musician_dicts = [
    {"id": 1, "fname": "Brian", "lname": "Wilson", "group": "Beach Boys"},
    {"id": 2, "fname": "Carl", "lname": "Wilson", "group": "Beach Boys"},
    {"id": 3, "fname": "Dennis", "lname": "Wilson", "group": "Beach Boys"},
    {"id": 4, "fname": "Bruce", "lname": "Johnston", "group": "Beach Boys"},
    {"id": 5, "fname": "Hank", "lname": "Marvin", "group": "Shadows"},
    {"id": 6, "fname": "Bruce", "lname": "Welch", "group": "Shadows"},
    {"id": 7, "fname": "Brian", "lname": "Bennett", "group": "Shadows"},
]

get_element_four = operator.itemgetter(4)
print(get_element_four(musician_dicts))

get_multiple_eliment = operator.itemgetter(1, 3, 5)
get_names = operator.itemgetter("fname", "lname")
print(get_multiple_eliment(musician_dicts))
print(get_names(musician_dicts))
'''Here itemgetter() creates a function that you use to find all three elements. Your function returns a tuple containing the results.'''

















