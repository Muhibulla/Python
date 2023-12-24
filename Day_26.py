# Closures

'''A closure in Python is a nested function that can access the variables of the outer function even after the outer function is finished. Closures are useful for creating inner functions, avoiding global variables, and improving code readability and performance.'''

def outer():
    x = 'Khan'

    a = 100
    def inner():
        a = 'Muhib'
        print("{0} is great".format(x))
    inner()
outer()


def outer():
    x = 'Khan'

    a = 100
    def inner():
        a = 'Muhib'
        print("{0} is great".format(x))
    return inner
fn = outer()

print(fn)

# It will show the free variables availeble in the functions.

fv = fn.__code__.co_freevars
print(fv)

# clousure, it will show the cell in python and the actual memory where variable is store

fc = fn.__closure__
print(fc)


def count():
    counter = 0
    def incr():
        nonlocal counter
        counter += 1
    return incr

f1 = count() # This will be point out the closure.
f2 = count()    

print(f1)

f1()



def adder(n):
    def inner(x):
        return n + x
    
    return inner

add_1 = adder(1)
add_2 = adder(2)
add_3 = adder(3)

print(add_1(10))
print(add_2(10))
print(add_3(10))

 

def max_multiplyer(n):
    def multiplyer(x):
        return x * n
    
    return multiplyer


mult3 = max_multiplyer(3)
mult5 = max_multiplyer(5)

print(mult3(3))
print(mult5(5))


def outer():
    numb = 1
    def inner():
        nonlocal numb
        numb += 2
        return numb
    return inner

odd = outer()

print(odd())
print(odd())
print(odd())
print(odd())

'''So what are closures good for?

Closures can be used to avoid global values and provide data hiding, and can be an elegant solution for simple cases with one or few methods. '''



def outer():
    x = "hey"
    def inner():
        y = "muhib"
        return x + y
    return inner

fn = outer()

print(fn.__code__.co_freevars)
print(fn.__closure__)



def outer():
    x = "python"

    def inner1():
        nonlocal x
        x = "extreme"
        print("this is", x)
    
    def inner2():
        nonlocal x
        x = "extreme"
        print("this is", x)

    return inner1, inner2

fn1, fn2 = outer()

print(fn1.__code__.co_freevars, fn2.__code__.co_freevars)
print(fn1.__closure__, fn2.__closure__)
print(fn1())

from time import perf_counter

class Timer:
    def __init__(self):
        self.start = perf_counter()

    def poll(self):
        return perf_counter() - self.start

t1 = Timer()

print(t1.poll())


def timer():
    start = perf_counter()
    def poll():
        return perf_counter() - start
    return poll

t1 = timer()

print(t1())

class Timer:
    def __init__(self):
        self.start = perf_counter()

    def __call__(self):
        return perf_counter() - self.start

t1 = Timer()

print(t1())






class Timer:
    def __init__(self) -> None:
        self.start = perf_counter()

    def pull(self):
       return perf_counter() - self.start
        
        
    
t1 = Timer()

print(t1.pull())







'''https://www.linkedin.com/pulse/decorators-inpython-can-arslan/'''



def greet(message):
    m = message
    def _inner(name):
        return f"{message} {name}"
    return _inner

g = greet("Hello, nice to meet you,")

print(g("khan"))
    





















