# Removing value from lists

animals = ["cat", "dog", "bear", "hourse", "monkey"]
animals_r   = animals.remove("dog")
print(animals)


# animals = ["cat", "dog", "bear", "hourse", "monkey"]
# animals_r   = animals.remove("elephant")
# print(animals)

# >>> ValueError: list.remove(x): x not in lis

# Sort method

"""
        sort() uses “ASCIIbetical order” rather than actual alphabetical
order for sorting strings. This means uppercase letters come before lower-
case letters. Therefore, the lowercase "a" is sorted so that it comes after the
uppercase "Z".

     """

value = [4, 2, 1, 3, 5]
value_s = value.sort()
print(value)

value = [4, 2, 1, 3, 5, -6, -9, 55]
value_s = value.sort()
print(value)

animals = ["cat", "dog", "bear", "hourse", "monkey"]
animals_s = animals.sort()
print(animals)
# >>> ['bear', 'cat', 'dog', 'hourse', 'monkey']
# reverse function can take arguments

animals = ["cat", "dog", "bear", "hourse", "monkey"]
animals_s = animals.sort(reverse=True)
print(animals)

# >>> ['monkey', 'hourse', 'dog', 'cat', 'bear']

#name_of_animals = [1, 4, 3, 2, 77, 'monkey', 'hourse', 'dog', 'cat', 'bear']
#name_of_animals_s = name_of_animals.sort()
#print(name_of_animals)

# >>> TypeError: '<' not supported between instances of 'str' and 'int'
# Python does not know string and intigers values

# 1. What is []?
# In python square bricket contain list data


""" 2. How would you assign the value 'hello' as the third value in a list stored
in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)For the following
 three questions, let’s say spam contains the list ['a','b', 'c', 'd'] """

#spam = ['a','b', 'c', 'd']
#spam_a = spam.insert(1, 'hello')
#print(spam)

# 3. What does spam[int(int('3' * 2) // 11)] evaluate to?
spam = int('3' * 2) // 11
spam_e = str(spam)
print(spam_e)
# >>> 3

# 4. What does spam[-1] evaluate to?
# It will select the last element of the list

# 5. What does spam[:2] evaluate to?
# It will select all the elemnt in the list till index `2` but not including `2`.














































