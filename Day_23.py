'''The reduce() function in Python is a built-in function that applies a given function to the elements of an iterable, reducing them to a single value. The syntax for reduce() is as follows:

functools.reduce(function, iterable[, initializer])

The function argument is a function that takes two arguments and returns a single value. The iterable argument is an iterable object such as a list, tuple, or generator. The optional initializer argument is a value that is placed before the elements of the iterable in the calculation.

The reduce() function works by applying the function to the first two elements of the iterable, then applying the function to the result and the next element, and so on until the iterable is exhausted. The final result is returned by the function.

For example, if you want to calculate the sum of a list of numbers, you can use reduce() with the addition operator as the function:

import functools
numbers = [1, 2, 3, 4, 5]
sum = functools.reduce(lambda x, y: x + y, numbers)
print(sum) # 15

Here, the lambda function takes two arguments x and y and returns their sum. The reduce() function applies this function to the elements of the numbers list, starting from the left. The calculation is as follows:

- First, the function is applied to 1 and 2, and the result is 3.
- Next, the function is applied to 3 and 3, and the result is 6.
- Next, the function is applied to 6 and 4, and the result is 10.
- Next, the function is applied to 10 and 5, and the result is 15.
- Since there are no more elements in the list, the final result is 15 and it is returned by the reduce() function.

You can also use a predefined function or an operator function instead of a lambda function. For example, you can use the operator.add function from the operator module to perform the same calculation as above:

import functools
import operator
numbers = [1, 2, 3, 4, 5]
sum = functools.reduce(operator.add, numbers)
print(sum) # 15

The initializer argument is useful when you want to provide a default value for the reduction or when the iterable is empty. For example, if you want to calculate the product of a list of numbers, you can use reduce() with the multiplication operator as the function and 1 as the initializer:

import functools
import operator
numbers = [1, 2, 3, 4, 5]
product = functools.reduce(operator.mul, numbers, 1)
print(product) # 120

Here, the initializer argument is 1, which means that the calculation starts with 1 as the first argument. The calculation is as follows:

- First, the function is applied to 1 and 1, and the result is 1.
- Next, the function is applied to 1 and 2, and the result is 2.
- Next, the function is applied to 2 and 3, and the result is 6.
- Next, the function is applied to 6 and 4, and the result is 24.
- Next, the function is applied to 24 and 5, and the result is 120.
- Since there are no more elements in the list, the final result is 120 and it is returned by the reduce() function.

If the initializer argument is not provided and the iterable is empty, then the reduce() function will raise a TypeError exception. For example, if you try to calculate the sum of an empty list without an initializer, you will get an error:

import functools
import operator
numbers = []
sum = functools.reduce(operator.add, numbers)
# TypeError: reduce() of empty sequence with no initial value

To avoid this error, you can provide a default value for the sum, such as 0, as the initializer argument:

import functools
import operator
numbers = []
sum = functools.reduce(operator.add, numbers, 0)
print(sum) # 0

The reduce() function can be used to perform various operations on iterables, such as finding the minimum or maximum value, checking if all or any values are true, concatenating strings, and so on. However, there are also alternative ways to achieve these tasks in Python, such as using built-in functions, comprehensions, or generators. These alternatives may be more readable, efficient, or Pythonic than using reduce(). You can learn more about them in the following resources:

- [Python's reduce(): From Functional to Pythonic Style](^2^)
- [reduce() in Python](^3^)

Source: Conversation with Bing, 11/20/2023
(1) Python's reduce(): From Functional to Pythonic Style. https://realpython.com/python-reduce-function/.
(2) reduce() in Python - Javatpoint. https://www.javatpoint.com/reduce-in-python.
(3) reduce() in Python - GeeksforGeeks. https://www.geeksforgeeks.org/reduce-in-python/.'''



# python code to demonstrate working of reduce() 

# importing functools for reduce() 
import functools 
import operator
from functools import reduce




# initializing list 
lis = [1, 3, 5, 6, 2] 

# using reduce to compute sum of list 
print("The sum of the list elements is : ", end="") 
print(functools.reduce(lambda a, b: a+b, lis)) 

# using reduce to compute maximum element from list 
print("The maximum element of the list is : ", end="") 
print(functools.reduce(lambda a, b: a if a > b else b, lis)) 



new_list = [40, 65, 88, 74]

print(functools.reduce(operator.add, new_list))
print(functools.reduce(operator.mul, new_list))
print(functools.reduce(operator.add, ["muhib ", "love ", "python. "]))


numbers = [0, 1, 2, 3, 4]

print(reduce(lambda x, y: x + y, numbers))
print(reduce(lambda x, y: x + y, numbers, 100))
print(reduce(lambda x, y: x * y, numbers ))
print(reduce(operator.mul, numbers))

numbers = [3, 5, 2, 4, 7, 1]

 
new_list = [40, 65, 88, 74]
product =  reduce(lambda x, y: x * y, new_list)
print(f"Product of {product} is")

new_list = [40, 65, 88, 74]
new_str = ["muhib ", "love ", "python. "]

oprator_add = reduce(operator.add, new_list)
operator_str = reduce(operator.add, new_str)


oprator_concat_str = reduce(operator.concat, new_str)


print(f"the addition of intergers are: {oprator_add}")
print(f"the addition of strings are: {operator_str}")

print(f"the concat of strings are: {oprator_concat_str}")



def square(x):
    return x ** 2

number = [1, 2, 3, 4, 5]

square_r = map(square, number)
print(list(square_r))

#call list() on map() to create a list object containing the square values

str_nums = ["4", "8", "-6", "-5","0", "3", "2", "8", "9", "2", "5"]
int_nums = map(int, str_nums)
new_list = list(int_nums)
new_lsit_square = list(map(lambda x: x ** 2, new_list))
print(new_lsit_square)

zip_list = list(zip(int_nums, new_lsit_square))
print(zip_list)


abs_nums = list(map(abs, new_lsit_square))
print(abs_nums)


str_nums = ["4", "8", "-6", "-5","0", "3", "2", "8", "9", "2","5.2", "3.2", "5"]
 
abs_nums = list(map(float, str_nums))
print(abs_nums)


str_nums = ["4", "8", "-6", "-5","0", "3", "2", "8", "9", "2","5.2", "3.2", "5"]
def change_condition(x):
    for value in x:
        if type(value) is str: 
            return list(map(float, x))
        elif type(value) is float:
            return list(map(int, x))
    else: 
        return list(map(abs, x))

print(change_condition(str_nums))


str_value = ["processing", "strings", "with", "map"]

new_str_val = list(map(str.capitalize, str_value))
print(new_str_val)
        
new_str_val = list(map(str.casefold, str_value))
print(new_str_val)

new_str_val = list(map(str.upper, str_value))
print(new_str_val)

new_str_val = list(map(str.encode, str_value))
print(new_str_val)




