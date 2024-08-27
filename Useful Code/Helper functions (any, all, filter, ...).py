'''
any(iterable)
Returns True if at least one element in the iterable is true; otherwise, returns False
'''
array = [1, 3, 5, 7]
has_even = any(x % 2 == 0 for x in array)
print(has_even)  # Output: False


'''
all(iterable)
Returns True if all elements in the iterable are true; otherwise, returns False
'''
nums = [1, 2, 3, 4]
is_consecutive = all(nums[j]+1 == nums[j+1] for j in range(len(nums)-1))
print(is_consecutive)  # Output: True


'''
filter(function, iterable)
Filters elements in the iterable, returning only those for which the function returns True
'''
filtered = list(filter(lambda x: x > 1, [0, 1, 2, 3]))
print(filtered)  # Output: [2, 3]


'''
map(function, iterable)
Applies a function to all elements in the iterable and returns a new iterable with the results
Similar to list comprehensions.
'''
doubled = list(map(lambda x: x * 2, [1, 2, 3]))
print(doubled)  # Output: [2, 4, 6]


'''
reduce(function, iterable)
Applies a function cumulatively to the elements of the iterable, reducing them to a single value
(requires functools module). Can also take a starting value.
'''
from functools import reduce
product = reduce(lambda x, y: x * y, [1, 2, 3, 4])
print(product)  # Output: 24

product = reduce(lambda x, y: x * y, [1, 2, 3, 4], 100)
print(product)  # Output: 2400


'''
count(value)
Returns the number of occurrences of value in a list or another iterable that supports it
'''
occurrences = [1, 2, 2, 3].count(2)
print(occurrences)  # Output: 2


'''
zip(iterable1, iterable2, ...)
Combines elements from multiple iterables, producing tuples of corresponding elements
'''
zipped = list(zip([1, 2, 3], [4, 5, 6]))
print(zipped)  # Output: [(1, 4), (2, 5), (3, 6)]


'''
sum(iterable)
Returns the sum of all elements in the iterable
'''
total = sum([1, 2, 3, 4])
print(total)  # Output: 10

total = sum((1, 2, 3, 4))
print(total)  # Output: 10


'''
sorted(iterable, key=None, reverse=False)
Returns a sorted list of the iterable’s elements
'''
sorted_list = sorted([3, 1, 2])
print(sorted_list)  # Output: [1, 2, 3]


'''
enumerate(iterable, start=0)
Returns an iterator of tuples containing index and element pairs
'''
enumerated = list(enumerate(['a', 'b', 'c']))
print(enumerated)  # Output: [(0, 'a'), (1, 'b'), (2, 'c')]

'''
round(number, ndigits=None)
Returns the number rounded to ndigits precision after the decimal point. If ndigits is omitted or None, it returns the nearest integer.
'''
rounded_number = round(3.14159, 2)
print(rounded_number)  # Output: 3.14

rounded_integer = round(3.75)
print(rounded_integer)  # Output: 4


'''
str.replace(old, new, count=-1)
Returns a copy of the string where all occurrences of the substring old are replaced with the substring new. If the optional argument count 
is given, only the first 'count' occurrences are replaced.
'''
replaced_string = "hello world".replace("world", "there")
print(replaced_string)  # Output: "hello there"

limited_replace = "hello hello hello".replace("hello", "hi", 2)
print(limited_replace)  # Output: "hi hi hello"

# Replacing all occurrences of a single letter
all_letters_replace = "banana".replace("a", "o")
print(all_letters_replace)  # Output: "bonono"
