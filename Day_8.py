def is_phone_number(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

#print(is_phone_number('415-555-4242'))
#print( is_phone_number("mushi mushi"))


message = "the office phone number is '245-254-2552'. You can call anyime."
for i in range(len(message)):
    chunk = message[i:i+12]
    if is_phone_number(chunk):
        print("Phone Number is found: " +  chunk)

print("Done")


import re

phon_number = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo = phon_number.search("My office phone number is 452-254-2551")
print("phone number found using regix: " + mo.group())


def clever_fun():
    print("wellcome")

clever_fun()

def add_numb(numb1: int, numb2: int) -> int:
    numb3 = numb1 + numb2
    return numb3

print(add_numb(3, 5))

def prime(n):
    if n in [2, 3]:
        return True
    if (n == 1) or (n % 2 == 0):
        return False
    r = 3
    while r * r <= n:
        if n % r == 0:
            return False
        r += 2
    return True
print(prime(78), prime(79))


def evenOdd(x):
    if x % 2 == 0:
        print("even")
    else:
        print("Odd")
evenOdd(45)
evenOdd(40)

pak_fruite = ["banana", "apple", "mango", "peach"]
chi_fruite = ["annanas", "mango", "orange", "something"]

def check_dup(pak_fruite, chi_fruite):
    seen_set = set()
    for item in pak_fruite:
        seen_set.add(item)
    for item in chi_fruite:
        if item in seen_set:
            return True
    return False
    

print(check_dup())
    










































