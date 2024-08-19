'''
Set is an unordered collection of unique elements.

Recommended to uncomment each print from top to bottom,
and run the code each time to understand.
'''

# CONSTRUCTORS
print('CONSTRUCTORS')
set1 = set()
set2 = {'a'}
set3 = set([10, 20, 30, 40])
set4 = set((20, 30, 40)) # stores each number, not the whole tuple
set5 = {(20, 30, 40)}  # stores the tuple, not each number

# print(set1)
# print(set2)
# print(set3)
# print(set4)
# print(set5)

# ADD
# print('\nADD')
# print(set1)
set1.add(42)
set1.add(35)
set1.update([10, 25, 36])  # Add many at a time
# print(set1)

# CHECK MEMBERSHIP
# print('\nCHECK MEMBERSHIP')
# print(35 in set1)  # True
# print(50 in set1)  # False


# REMOVE
# print('\nREMOVE')
set1.remove(35)   # raises error if 35 is not present
set1.discard(100)  # Doesn't raise an error if 100 is not present
# print(set1.pop())  # Removes and returns a random element, raises KeyError if empty
set1.clear()  # remove all
# print(set1)


# OPERATIONS
# print('\nOPERATIONS')
# Union, O(len(set1) + len(set2))
set1.update([30, 40, 50, 60])
set2.update(['b','c'])
union_set = set1 | set2
# print(union_set)

# Intersection, O(min(len(set1), len(set2)))
intersection_set = set1 & set3
# print(intersection_set)

# Difference, O(len(set1))
# print(sorted(list(set1)), sorted(list(set3)))
difference_set = set3 - set1
# print(difference_set)
# print(set1 - set3)
