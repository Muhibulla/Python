"""
Day 2: Strings to Integers
Write a function called convert_add that takes a list of strings
as an argument and converts it to integers and sums the list. For
example [‘1’, ‘3’, ‘5’] should be converted to [1, 3, 5] and
summed to 9.

"""

test_list = ['1', '4', '5']
def convert_add(data: list):
    for i in data:
        return int(i)
    
print(convert_add(test_list))

def convert_add(lst):
    return sum(int(i) for i in lst)

print(convert_add(test_list))

def convert_str_to_int(lst):
    return [int(i) for i in lst]

print(convert_str_to_int(test_list))


test_list2 = ['2', '4', '6']
def cov(list):
    return sum(int(i) for i in list)

print(cov(test_list2))


data = [(2, 'b'), (1, 'A'), (2, 'a'), (1, 'b'), (3, 'c'), (3, 'C')]

sorted = sorted(data, key= lambda s: [s.upper()])
print(sorted)