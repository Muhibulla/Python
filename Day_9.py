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

print(is_phone_number('415-555-4242'))
print( is_phone_number("mushi mushi"))


message = "the office phone number is '245-254-2552'. You can call anyime."
for i in range(len(message)):
    chunk = message[i:i+12]
    if is_phone_number(chunk):
        print("Phone Number is found: " +  chunk)

print("Done")


import re

phon_number = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

match_object = phon_number.search("My office phone number is 452-254-2551")
print("phone number found using regix: " + match_object.group())

regex_petern = r'\+\d{5}-\d{7}'
ro = re.compile(regex_petern)
match = ro.search("my pakistani number is +92305-8141471")
if match:
    print("you first regix work here is number: " + match.group())
else:
    print("not working")


a_message = "In america number a as follow standerd 123-456-7890"
regex_p = r'\d{3}-\d{3}-\d{4}'
match_o = re.compile(regex_p)
match_a = match_o.search(a_message)
print("Your regex work as per american standerd here is the Number: " + match_a.group())

phoneNumberregex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo_2 = phoneNumberregex.search('My number is 123-456-4789')
print(mo_2.group(1))
print(mo_2.group(2))
print(mo_2.group())

#perantheses = re.compile(r'(\(\d{3}))-(\d{3})-(\d{4})')
#mo_p = perantheses.search("I want to search perantheses is this number (223-123-4563")
#print("Your pera is fount: " + mo_p.group())

hero_regex = re.compile(r'(Batman )| (Jiya)')
mo_h = hero_regex.search("I want to search Batman in this string")
print(mo_h.group())





















