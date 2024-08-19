'''
You can put an else after a try-except. It will run only if no exception happens.
In other words, if the code in the try block runs to completion without any problems.
If any exception happens, the else will be ignored.

It must always come after 'except' and before 'finally'.
'''

try:
    a = 1 / 0
except ZeroDivisionError:
    print("You can't divide by 0")
else:
    print("This will print if no exception occurred")
'''
Output:
You can't divide by 0
'''


try:
    a = 1 / 1
except ZeroDivisionError:
    print("You can't divide by 0")
else:
    print("This will print if no exception occurred")
'''
Output:
This will print if no exception occurred
'''
