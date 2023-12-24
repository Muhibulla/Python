

tuple = 10, 50, 70, 50, 60, "a", 33

def print_tuple(t):
    for e in t:
        print(e)

print_tuple((10, 50, 40, 20))
print_tuple(tuple)
print(tuple[:5])

a = 1,2,3,4,5
x, *other, y, z = a
print(x,  other, y, z)

# Python is immutable, we can not change the tuple but we can definatly

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.__class__.__name__}(x={self.x}, y={self.y})"

pt = Point2D(10, 20)

print(pt)

print(id(pt)) 

pt.x = 100

print(pt)

print(id(pt))



karachi = "karachi", "pakistan", 2_100_000
delhi = "delhi", "india", 3_100_000
kabul = "kabul", "afghanistan", 100_100

cities = [karachi, delhi, kabul]

total = 0

for population in cities:
    total += population[2]

print(total)

total = sum([population[2] for population in cities])
print(total)


tuple = 10, 50, 70, 50, 60, "a", 33

a, *_, b, c = tuple

print(a, b, c)

for city in enumerate(cities): # enumerate is a built in function in python that return tuple.
    print(city)



def is_palindrome(s):
   # s = s.lower().replace(' ', '')
    return s == s[::-1]

string = "civic"
result = is_palindrome(string)

if result:
    print(f'{string} is a palindrome.')
else:
    print(f'{string} is not palindrome.')













