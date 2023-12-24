# Decorators

'''A decorator is nothing but a wrapper around a function in Python. It takes the function of interest as an argument, performs certain tasks before and after calling it and returns the results.'''

import time



def timer(func):
    def wrapper(*args, **kwards):
        start = time.time()
        result = func(*args, **kwards)
        end = time.time()

        print(f"{func.__name__} has run { end - start} seconds.")
        return result

    return wrapper

def make_multiplayer(n):
    def multiply(x):
        return n * x
    return multiply


time3 = make_multiplayer( 5)
print(time3(5))



def decorator(func):
    def wrapper():
        print("something is happen before function.")
        func()
        print("after.")

    return wrapper
@decorator
def say():
    print("hello")

print(say())

def counter(fn):
    count = 0
    def increment(*args, **kwards):
        nonlocal count 
        count += 1
        print("the function {0} (id={1}) has run {2} times", count )
        return fn(*args, **kwards)
    return increment

def add(a: int, b: int=0):
    """
    This function will return addition of two values.

    """
    return a + b

print(id(add))

add = counter(add)

print(id(add))

print(add(20, 50))

print(add(20, 40))


@counter
def my_func(s: str, i: int) -> str:
    return s * i
 
print(my_func("a", 5))









