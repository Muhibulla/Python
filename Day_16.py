

def a():
    print('a() start' )
    b()
    c()
    print('a() return')
def b():
    print('b() start')
    print('a() return')
def c():
    print('c() start')

a()

def spam():
    eggs = 99
    bacon()
    print(eggs)
def bacon():
    ham = 101
    eggs = 0
spam()


def spaN():
    print(eggs)
eggs = 42
spaN()
print(eggs)

def spak():
    global eggs
    eggs = "spak"
eggs = "global"
spak()
print(eggs)


#def zerDividedpy(divideby):
 #   try:
 #       return 42 / divideby
 #   except ZeroDivisionError:
 #       print('Error: Invalid argument')
#print(zerDividedpy(2))
#print(zerDividedpy(4))
#print(zerDividedpy(0))
#print(zerDividedpy(9))

import pyinputplus as pyip

class Student():
    def __init__(self, name, emailAddress, currentGrade ):
        self.name = name 
        self.emailAddress = emailAddress 
        self.currentGrade = currentGrade 
    def show(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.emailAddress}")
        print(f"Grade: {self.currentGrade}")
    def __str__(self) -> str:
        return f"Studen(Name = {self.name}, email = {self.emailAddress}, Grade = {self.currentGrade})"

#student1 = Student("muhib", "muhibullah@gmail", "10A")
#student2 = Student("moiz", "moiz@gmail.com", "10b")

#print(student1)
#student1.show()
#print(student2)


# at this poit integrate with library (pyinput plus)

name = pyip.inputStr(f"Please type your Name.")
emailAddress = pyip.inputEmail (f"Please provide your email address.")
currentGrade = pyip.inputChoice(["10-A", "10-B", "10-C"])

student = Student(name, emailAddress, currentGrade)
















