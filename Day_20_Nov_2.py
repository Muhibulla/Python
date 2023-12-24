

"""
def time_it(fn, *args, **kwrds):
    print(args, kwrds)

time_it(print(1,2,3 , sep=" - ", end=" ***"))
time_it(print, 1,2,3 , sep=" - ", end=" ***")
"""


def time_it(fn, *args, **kwards):
    fn( *args, **kwards)

'''
time_it(print, 1,2,3 , sep=" - ", end=" ***")

def time_it(fn, *args, rep=1, **kwards):
    for i in range(rep):
        fn( *args, **kwards)


time_it(print, 1,2,3 , sep=" - ", end=' ***', rep=5)
'''
test_list = ['apple', 'banana', 'mango', 'thelongesvalue']
test_dict = {'fruite':'apple', 'juice': 'banana'}
'''
def longest(d: dict):
   
    longest_value = max(d.values(), key=len)
    return longest_value
    
print(longest(test_list))
'''
def longest_value(data):
    '''Return the longest value from a list or dictionary'''
    if isinstance(data, dict):
        values = list(data.values())
    elif isinstance(data, list):
        values = data
    else:
        raise TypeError('Input must be a list or dictionary')
    longest_value = max(values, key=len)
    return longest_value

print(longest_value(test_list))





def the_longest(data):
    if isinstance(data, dict):
        values = list(data.value())
    elif isinstance(data, list):
        values = data
    else:
        print('something')
    



