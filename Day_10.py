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


bat_regis = re.compile(r'bat(wo)*man')
#mo_b = bat_regis.search("the movie batwoman was good")
#mo_b = bat_regis.search("the movie batwoman was good")
mo_b = bat_regis.search("the movie batwowowowoman was good")
print(mo_b.group())

bat_regis = re.compile(r'bat(wo)+man')
#mo_b = bat_regis.search("the movie batwoman was good")
#mo_b = bat_regis.search("the movie batwoman was good")
mo_b = bat_regis.search("the movie batwowowowoman batwoman batman was good")
print(mo_b.group())


greedy_regex = re.compile(r'(ha){3,5}')
mo_g = greedy_regex.search('hahahahahahahah')
print(mo_g.group()) # >>> hahahahaha

non_greedy_regex = re.compile(r'(ha){3,5}?')
mo_n = non_greedy_regex.search('hahahahahah')
print(mo_n.group()) # >>> hahaha


phoneNumberregex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo_s = phoneNumberregex.search('My number is 123-456-4789 and my office number is 987-654-1234')
print(mo_s.group())

phoneNumberregex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo_f = phoneNumberregex.findall('My number is 123-456-4789 and my office number is 987-654-1234')
print(mo_f)

findall_regex = re.compile(r'batman | superman')
mo_fa = findall_regex.findall("I want to find superman and batman in this string")
print(mo_fa)


fruit_list = ["apple", "bnana", "mango", "ananaas", "pinapple", "graps"]
fruite_regex = re.compile(r'apple | pinapple')
mo_fr = fruite_regex.findall("I want to find apple and pinapple in this string. And ignore greps.")
print(mo_fr)

xmas_regex = re.compile(r'\d+\s\w+')
mo_x = xmas_regex.findall("I want to find 12 bnanas, 11 humenbeing, 2 dove soup")
print(mo_x)

voval_regex = re.compile(r'[aeiouAEIOU]')
mo_v = voval_regex.findall("I want to find all the vovals in this line string. Also bAby FoOd")
print(mo_v)


'''By placing a caret character (^) just after the character class’s opening
bracket, you can make a negative character class. A negative character class
will match all the characters that are not in the character class'''

#voval_regex = re.compile(r'[^aeiouAEIOU]')
#mo_v = voval_regex.findall("I want to find all the vovals in this line string. Also bAby FoOd")
#print(mo_v)

#voval_regex = re.compile(r'[a-zA-Z0-5]')
#mo_v = voval_regex.findall("I want to find all the alphabats and a number 9")
#print(mo_v)

#voval_regex = re.compile(r'[a-zA-Z0-5]')
#mo_v = voval_regex.findall("I want to find all the alphabats and a number 4")
#print(mo_v)


class person:
    def __init__(self):
        pass
        self.hight = 130
        self.weight = "40 kg"
        self.name = "muhib"

    def detail(self):
        print(f'Hello {self.name} your hight {self.hight} is very attractive and your {self.weight} is also in controll.')
        
person_instance = person()

person_instance.detail()

print(person_instance.hight)
print(type(person_instance))


class tution:
    def __init__(self) -> None:
        self.language = 'Python'
        self.time = '2 months'
        self.duration = '2 hours'
    def details(self):
        print(f"The {self.language} is the best language and it require {self.time} and minimum {self.duration} on daily bases")

tution_instance = tution()
tution_instance.details()


class Program:
    language = 'Python'
    def say_hello():
        print(f"The {Program.language} is now becoming easy.")

Program.say_hello()













