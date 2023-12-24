#Write a Python function to find the maximum of three numbers


def maximum_of_three(x, y, z):
    return max(x, y, z)


print(f'The maximum number in given numbers is:', maximum_of_three(10, 125, 555))


def ret_max_list(input_list):
    if len(input_list) == 0:
        return None
    else:
        return max(input_list)

my_list = [55, 66, 77, 88]
print(f' The max number from given list is: ', ret_max_list(my_list))

my_str = ["banana", "apples", "mangoes"]

ret_max_str = print(f"the longest string: ", ret_max_list(my_str))


sum_list = [2, 4, 6, 8]  
def sumb(list_numb):
    if len(list_numb) == 0:
        return None
    else:
        return sum(list_numb)
    

  
print(f'The summison is: ', sumb(sum_list))
new_list = [8,2,3,0,7]
print(f'The summison is: ', sumb(new_list))


def multiply(input_list):
    result = 1
    for number in input_list:
        result *= number
    return result
sample_list = [8, 2, 3, -1, 7]
print(f'The answer is : ', multiply(sample_list) )


def multip(input_number):
    result = 1
    for number in input_number:
        result *= number
    return result

sample_list = [2, 5, 6, 7, 5]

print(f'The result from 2nd:', multip(sample_list))


def reverse(input_str):
    reverse_str = input_str[:: -1]
    return reverse_str
    
sample_list = "Orignal string"
print(reverse(sample_list))


def factorail_number(n):
    if n == 0:
        return 1
    else:
        return n * factorail_number(n - 1)

number = 8 
result = factorail_number(number)

print(f'The factorail number of {number} is {result}.')

s = {10, 99, -3, 'd'}
print(s)

l1 = [1, 2, 4, 5,]
a, b, *c, = l1
print(a)
print(b)
print(c)


l1 = ['something', 4, 6, 'everything', [1, 4, 6, 7,]]
a,  b, *c, (e, *d) = l1
print(a)
print(b)
print(c)
print(d)
print (type(e))



number = [1, 2, 3 ,4, 5, 6, 7,]
first, *last = number
print(first)
print(last)



test_dic = {"kyte":3, "name":33, "string":4, "baby": 5}
a, b, *rest = test_dic
print(a)
print(b)
print(rest)

number = [1, 2, 3 ,4, 5, 6, 7,]

a, b = number[0], number[1:]
print(a)
print(b)


str1 = "khan"
str2 = "Moiz"
l = [*str1, *str2]
l2 = {*str1 , *str2}
print(l)
print(l2)

def func1(input_str):
    reverse = input_str[:: -1]
    return reverse

str = ["lsit", "of", "strings", "that"]

print(func1(str))



def range_checker(input_numb):
    range = 0-10
    if input_numb > 10:
        print(f"Number not allowed.")
    else:
        return
    print(f"it's OK.")


print(range_checker(8))
print(range_checker(12))
print(range_checker(14))
print(range_checker(5))


def range_check(n):
    if n in range(0,9):
        print(f" {n} is in range")
    else:
        print(f" The {n} is outside given range.")
range_check(2)
print(range_check(5))
print(range_check(13))
print(range_check(3))


def string_upper(input_sting):
    d = {"U_C":0, "L_C":0}
    for c in input_sting:
        if c.isupper():
            d["U_C"]+=1
        elif c.islower():
            d["L_C"]+=1
        else:
            pass
    print("orignal string is :", input_sting)
    print("no. of upper case : ", d["U_C"])
    print("no. of lower case : ", d["L_C"])

string = "The foX is Dancing"
string_upper(string)

def upperCase(input_string):
    U_C = 0
    L_C = 0

    for char in input_string:
        if char.isupper():
            U_C += 1
        elif char.islower():
            L_C += 1
    return U_C, L_C

input_string = "heLLo worlD"
U_C, L_C = upperCase(input_string)
print(f"Uppercase is No. {U_C}")
print(f"Lowercase is No. {L_C}")





class Account():
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = int(balance)
        self.password = password

    
    def deposit(self, amountToDeposit, password):
        if password == password :
            print(f"Your password in incorrect.")
            return None
        
        if amountToDeposit < 0:
            print(f"You can not deposit negative amount, Thanks.")
            return None
        self.balance = self.balance + amountToDeposit
        return self.balance



    def widraw(self, amountTowidraw, password):
        if password == password:
            print(f"Your password in incorrect.")
            return None
        elif amountTowidraw > self.balance:
            print(f"You do not have sufficiant Ballance.")
            return None
        else:
            if amountTowidraw < 0:
                print(f"You can not widraw Negative Balance")
        self.balance = self.balance - amountTowidraw
        return self.balance
    
    def getBalance(self, balance, password):
        if  password == password:
            print(f"Your password in incorrect.")
            return None
        return self.balance

    def show(self, name, balance):
        print(f"Wellcome {name} Your Balance is")
        print(f"{self.balance}")


        
        











































































