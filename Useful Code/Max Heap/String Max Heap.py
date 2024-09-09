'''
Max = closest to Z.
'''
from heapq import heapify, heappop as pop, heappush as push

names = ['sarah', 'david', 'zack', 'xavier', 'carlos', 'alice', 'ethan', 'fred']

class Str(str):
    def __lt__(self, other):
        return self > other

max_heap = [Str(name) for name in names]
heapify(max_heap)

for name in ['bob', 'rick', 'oscar', 'yasmin', 'george', 'peter']:
    push(max_heap, Str(name))

for _ in range(len(max_heap)):
    p = pop(max_heap)
    # p is of type 'Str', it can be converted back with str(p)
    print(p)

'''
Output:
zack
yasmin
xavier
sarah
rick
peter
oscar
george
fred
ethan
david
carlos
bob
alice
'''
