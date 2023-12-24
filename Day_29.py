

from collections import namedtuple



'''It’s important to note that, while tuples and named tuples are immutable, the values they store don’t necessarily have to be immutable.


It’s totally legal to create a tuple or a named tuple that holds mutable values:'''

Point = namedtuple("Point", ["x", "y"])

# print(Point)
# Point(2, 4)
# print(Point)



# # A str with comma seprated field names.
# Point = namedtuple("Point", "x, y")

# point = Point

# print(point)

# Point(8, 10)

# print(Point)



# class Point:
#     def __init__(self, x, y):
#         self.x = x 
#         self.y = y

# point2 = Point

# print(point2)


# Developer = namedtuple(
#      "Developer",
#      "name level language",
#      defaults=["Junior", "Python"]
# )

# print(Developer("jhon"))

# tuple_1 = ("something", 2018, 1 , 25, 26_313, 26_485, 26_556)

# pre = tuple_1[:3]
# post = tuple_1[:5]

# tuple_2 = pre + (26,) + post

Person = namedtuple("Person", "name age height")

person1 = Person("Khan", 26, 5.5)

person2 = Person._make(["Moiz", 25, 4.5]) #  '''Note that ._make() is a class method that works as an alternative class constructor and returns a new named tuple instance.'''

print(person2)

person3 = Person("Alhamd", 22, 4.2)

alhamd = person3._asdict() #When you call ._asdict() on a named tuple, you get a new dict object that maps field names to their corresponding values in the original named tuple. The order of key value  pairs are also same.
print(alhamd)
 






Point = namedtuple('Point', 'x y')
pt = Point(10, 25)
print(pt)
print(pt.x)
print(pt.y)

# pt[0] = 20 #TypeError: 'Point' object does not support item assignment

print(id(pt))
 
pt = Point(pt.y, 20)

print(id(pt))
print(pt)

pt = pt._replace(x = 20)

print(pt)
print(id(pt))


# Basic Namedtuple Creation
''' Create a named tuple called `Person` with fields `name`, `age`, and `gender`. Create instances of this named tuple and print their attributes.'''

Person = namedtuple("Person", "name age gerder")

khan = Person("khan", 25, "Male")
hira = Person("hira", 21, "Female")

print(khan, hira)

# Modify Field Values 
'''Create a named tuple and then modify one of its field values. Print the updated named tuple.'''

Person_modify = namedtuple("Person", "name age gerder")
khan = Person("khan", 25, "Male")
khan = khan._replace(age = 26)
print(khan)








