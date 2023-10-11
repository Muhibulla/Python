'''The findall() method returns a list of strings or a list of tuples of
strings. What makes it return one or the other? '''

''' Findlall will return a list if group is not used while in group it will return tuple '''

''' 6. Parentheses and periods have specific meanings in regular expression
syntax. How would you specify that you want a regex to match actual
parentheses and period characters?'''

''' 
The `\(`  `\)` escape characters in the raw string passed to re.compile()
will match actual parenthesis characters. 
Special charactors like `.` \. '*' \* and so on

'''
import re

#text = '("Parentheses")("group2")'
#mo = re.search(r"(\( 'Parantheses'\))('group2')", text)

#print(mo.group(2))


'''7. What does the | character signify in regular expressions?'''
'''When you use | in a regular expression pattern, it creates a logical OR between the subpatterns on either side of it. It means that the pattern will match if it finds a match for either the left-hand subpattern or the right-hand subpattern'''

''' 8. What two things does the ? character signify in regular expressions?'''
''' Non greedy use, example is ha{3, 5}? it will return as little as possible and return will be hahaha threee times
2nd is Optional when used like "colou?r" making u optional it will return color or colour'''


''' 11. What is the difference between {3} and {3,5} in regular expressions?'''
''' {3} will return item three time while {3, 5} will return item from 3 to 5.
{n} is a precise quantifier that requires an exact number of occurrences, while {m,n} allows for a range of occurrences within the specified limits '''



#while True:
#    print("Please input Your age")
#    age = input()
#    try:
#       age = int(age)
#    except:
#        print("Please use Numeric numbers.")
#        continue
#    if age < 1:
#        print("Please enter Positive Number.")
#        continue
#    break
#print(f"Your are {age} years old.")

import pyinputplus as pyip

#responseNumb = pyip.inputInt(prompt='Enter your number ', allowRegexes=[r'(I|V|X|L|D|M|C)+,'r'zero'])
#otN = responseNumb
#print(otN)

mystring = "this is string"
print(type(mystring))

class DimmerSwitch():
    def __init__(self) -> None:
        self.swichIsOn = False
        self.brightness = 0
    
    def turnOn(self):
        self.swichIsOn = True
    def turnOff(self):
        self.swichIsOn = False
    def raiseLevel(self):
        if self.brightness < 10:
            self.brightness = self.brightness + 1
    def decreaseLevel(self):
        if self.brightness > 1:
            self.brightness = self.brightness - 1
    def show(self):
        print('Switch is On?', self.swichIsOn)
        print('Brightness is:', self.brightness) 
oDimmer = DimmerSwitch()


oDimmer.turnOn()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.show()

oDimmer.decreaseLevel()
oDimmer.decreaseLevel()
oDimmer.turnOff()
oDimmer.show()



class Person():
    def __init__(self) -> None:
        print(f'New class is initaited by name: {self}.')
p = Person()
print(p)
print(hex(id(p)))

inpDte = pyip.inputDatetime(prompt="please Input Date For: day month year", formats=('%m%d%y %H:%M','%m%d%y %H:%M'))

inp = pyip.inputStr(prompt="Enter alphabates...", blank=True, blockRegexes= "aeiou")
print(inp)

inpInt = pyip.inputInt(prompt="Enter some Numbers...", default=0, max=3, limit=3)
print(inpInt)


inpMnu = pyip.inputMenu(["apple", "mango", "orange"])
print(inpMnu)





























