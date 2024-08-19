'''
nonlocal
Lets you edit variables outside of an inner function
'''
def sample():
    name = 'David'
    age = 27
    friends = ['James', 'Peter', 'Jane']

    print(name, age, friends)  # David 27 ['James', 'Peter', 'Jane']

    def inner():
        # This line lets you edit name and age
        # Otherwise, they would only be readable
        # and trying to edit would just create a temporary one separate from the original, or throw error
        nonlocal name, age

        name = 'John'
        age = 30
        age += 1

        # arrays (and mutable objects) can already be changed on the inside
        friends.append('Susan')

        # just not their reference
        # friends = [] # causes UnboundLocalError to be raised
        
        print(name, age, friends)  # John 31 ['James', 'Peter', 'Jane', 'Susan']

    inner()

sample()


'''
global
The same concept applies to functions trying to edit variables
with a global scope.
'''
name = 'David'
age = 27
friends = ['James', 'Peter', 'Jane']

print(name, age, friends)  # David 27 ['James', 'Peter', 'Jane']

def sample():
    # This line lets you edit name and age
    # Otherwise, it would only be readable
    # and trying to edit would just create a temporary one separate from the original, or throw error
    global name, age

    name = 'John'
    age = 30
    age += 1

    # arrays (and mutable objects) can already be changed on the inside
    friends.append('Susan')

    # just not their reference
    # friends = [] # causes UnboundLocalError to be raised

    print(name, age, friends)  # John 31 ['James', 'Peter', 'Jane', 'Susan']

sample()
print(name, age, friends)  # John 31 ['James', 'Peter', 'Jane', 'Susan']
