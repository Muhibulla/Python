# Find websites that start with http:// or https://

import re

text = '''You can visit our website at https://www.example.com for secure online shoppingYou can visit our website at https://www.example.com for secure online shopping."
"Please make sure to check the HTTP version of the website, http://www.example.org, for compatibility."
"The company's official blog can be found at https://blog.example.com, while their main site is http://www.example.net."
"For more information on the event, visit https://www.eventwebsite.com."
"You can access your email through the following link: https://mail.example.net."'''

webRegex = re.compile(r'https?://\S+', re.VERBOSE | re.I )
mo = webRegex.findall(text)
print(mo)


# re.compile(r'https?://\S+')
#re.compile(r'https?://\S+')
#re.compile(r'https?://\S+')
#re.compile(r'https?://\S+')
#re.compile(r'https?;//\S+')
#re.compile(r'https?;//\s+')
#re.compile(r'https?://\S+')
#re.compile(r'https?://\S+')
#re.compile(r'https?://\S+')


# What is the function that creates Regex objects?
# To create a regex function is compile() :example re.compile()

# Why are raw strings often used when creating Regex objects.
# To avoid unintended escaping of special characters.

#In the regex created from r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does
#group 0 cover? Group 1? Group 2?
groupRegex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
mo = groupRegex.search("this is mt phone number 123-456-7896")
print(mo.group())

def turnOn():
    global switchIsOn
    switchIsOn = True
def turnOff():
    global switchIsOn
    switchIsOn = False
switchIsOn = False

print(switchIsOn)
turnOn()
print(switchIsOn)
turnOff()

# 00_switch

class Lightswitch():
    def __init__(self) -> None:
        self.switchIsOn = False
    def turnOn(self):
        self.switchIsOn = True
    def turnOff(self):
        self.switchIsOn = False 
    def show(self):
        print(self.switchIsOn)

olightSwitch = Lightswitch()  # we have define object
olightSwitch.turnOn()
olightSwitch.show()
olightSwitch.turnOff()
olightSwitch.show()

class Person():
    def say_hello():
        print("hello")

print(Person.say_hello)
print(type(Person.say_hello))
Person.say_hello( )
p = Person

print(hex(id(p)))
print(p.say_hello)
































