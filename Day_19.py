# Keyword arguments


def func(a, b, c, *arg, d=100):
    print(a)
    print(b)
    print(c)
    print(arg)
    print(d)

print(func(1, 25 , 21, 3, 4, 5, d=10 ))

def name(name, age):
    print(f"hey {name} why you are {age} years old")
print(name("alice", 34))



def func(a, b, *arg):
    print(a)
    print(b)
    print(arg)

print(func('Muhib', 28, 85000, "Moiz steel", "something else."))

def mendatory_arg(d, *arg):
    print(arg)
    print(d)

print(mendatory_arg(40, "something", "test", 50, 50))

def mendatory_arg_rev(*arg, d):
    print(arg)
    print(d)

print(mendatory_arg_rev(40, "something", "test", 50, d=50))
mendatory_arg_rev("something else", "behind", 40, 20, d=21 )


def distinc(input_list):
    uniq = []
    for char in input_list:
        if char not in uniq:
            uniq.append(char)
    return uniq


test_list = [2,2,4,4,5,5]
print(distinc(test_list))

new_list =  [1,2,3,3,3,3,4,5, "let's try string", "let's try string", "muhib", "muhib"]
print(distinc(new_list))


'''Write a function called divide_or_square that takes one
argument (a number), and returns the square root of the number
if it is divisible by 5, returns its remainder if it is not divisible by
5. For example, if you pass 10 as an argument, then your function
should return 3.16 as the square root.'''

def devide_or_square(number):
    if number % 5 == 0:
        sq_root = number ** 0.5
        return f'The square root of provided number is {sq_root}.'
    else:
        reminder = number % 5
        return f'Reminder for the division is {reminder}'
    
print(devide_or_square(50))


















