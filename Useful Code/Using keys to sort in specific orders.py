'''
Recommended to comment all prints and try each one from start to finish to understand.
IDE: https://www.sololearn.com/en/compiler-playground/ccNJG4hN584J
All these examples can also be used with 'arr.sort(key= ...)'
'''
arr = [(9,4), (9,0), (3, 4), (-6,0), (-2, 12), (-7, 0), (4,0), (3, 6), (3, 0), (13,-5), (0,0), (1,0), (-7,0), (2, 5)]

# Sort by first element, then by second
print(sorted(arr))  # or arr.sort() to change the array

# Sort by second element, ignoring the first
print(sorted(arr, key=lambda x: x[1]))

# Sort by second element, then by first
print(sorted(arr, key=lambda x: (x[1], x[0])))


print('\nThree-value tuples:')
arr = [(9, 4, 1), (9, 0, 7), (3, 4, -2), (3, 0, 5), (-2, 12, 0), (-7, 0, 8), 
       (4, 0, 2), (3, 6, 3), (-6, 0, 5), (13, -5, -1), (0, 0, 6), (1, 0, -7), 
       (-7, 0, 9), (2, 5, -3)]

# Sort by second element, then by third, then by first
print(sorted(arr, key=lambda x: (x[1], x[2], x[0])))


'''
Using classes
'''
print('\nClasses:')
class Person:
    def __init__(self, name, age, height_cm):
        self.name = name
        self.age = age
        self.height_cm = height_cm
    
    def __repr__(self):
        return f'{self.name} {self.age} {self.height_cm}'


arr = [Person('David', 27, 168), Person('Bob', 56, 164), Person('Kim', 18, 155), 
        Person('Joanna', 17, 155), Person('Jane', 22, 150), Person('John', 30, 172), 
        Person('Daniel', 30, 204), Person('David', 27, 190)]

# Sort by age first, height second, and ignore name
print(sorted(arr, key=lambda p: (p.age, p.height_cm)))

# Sort only by height
print(sorted(arr, key=lambda p: p.height_cm))

# Sort by height, then, age, then name
print(sorted(arr, key=lambda p: (p.height_cm, p.age, p.name)))

# Sort by age reverse, then by name, then by height reverse
print(sorted(arr, key=lambda p: (-p.age, p.name, -p.height_cm)))
