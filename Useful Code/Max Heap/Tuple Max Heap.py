from heapq import heapify, heappop as pop, heappush as push

class MaxTuple(tuple):
    def __lt__(self, other):
        return self[0] > other[0]

my_tuples = [(2, "orange"), (0, "red"), (5, "blue"), (6, "yellow"), (4, "green")]

my_queue = [MaxTuple(t) for t in my_tuples]
heapify(my_queue)

for tup in [(1, "pink"), (3, "brown")]:
    push(my_queue, MaxTuple(tup))

while my_queue:
    print(pop(my_queue))

'''
Output:
(6, 'yellow')
(5, 'blue')
(4, 'green')
(3, 'brown')
(2, 'orange')
(1, 'pink')
(0, 'red')
'''
