

# Variables Globle and Local

'''Local variables are those that are defined inside a function and can only be used within that function and their scope is limited to that function only'''

'''Global variables are those that are defined outside any function and can be used by anyone, both inside and outside of functions. For example:'''

'''https://www.geeksforgeeks.org/global-local-variables-python/'''

x = "Aowsom" #Globle variable

def my_func():
    y = "fantastic" #Local variable
    print(f' Python is  ' + x + ' and ' + y)

my_func()


def my_func():
    #Local variable.
    x = 'I love python.'
    print(x)

my_func()

def f():
    x = "I love python"
    print("inside function", x)

f()
print("outside function", x) # Result # outside function Aowsom relate to code line #9
# Actual result would be NameError: name 's' is not defined.



x = "Python is learnable"

def f():
    y = "learning"
    print(y + "and " + x)

f()
print("outside of ", x)


s = "python is globaly good"
def func():
    s = "Pythin is good."
    print(s)

func()
print(s)


def inner_scop():
    x = "hello"
    def inner1():
        def inner2():
            nonlocal x
            x = "python"
            print(x)
        inner2()
    inner1()
inner_scop()


def outer():
    x = "Muhib"
    def inner1():
        x = "moiz"
        print("Value of x in inner", x)
        def inner2():
            nonlocal x
            x = "haram"
            print("Value of x in inner2", x)
        inner2()
    inner1()

    print("Vlue of x when local scop.", x)
outer()


def outer_func():
    x = "Khan"
    def inner():
        x = "Muhib"
        print("inner", x)
    inner()
    print("outer", x)
outer_func()


def outer_func():
    x = "Khan"
    def inner():
        nonlocal x
        x = "Muhib"
        print("inner", x)
    inner()
    print("outer", x)
outer_func()















