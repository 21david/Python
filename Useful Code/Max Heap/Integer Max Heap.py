from heapq import heapify, heappop as pop, heappush as push

nums = [5, -6, 20, -3, 5, 0, 12, 5]

# Reverse comparison to simulate a max heap
class Num(int):
    def __lt__(self, other_num):
        return self > other_num

# Heapify
max_heap = [Num(num) for num in nums]
heapify(max_heap)

# Pushing and popping
for n in [-5, 6, 3, 10, -4, 3, -6, 7, 8]:
    push(max_heap, Num(n))

for _ in range(len(max_heap)):
    print(pop(max_heap))

'''
Output:
20
12
10
8
7
6
5
5
5
3
3
0
-3
-4
-5
-6
-6
'''
