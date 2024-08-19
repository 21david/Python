from itertools import product
R = 5  # 5 rows
C = 3  # 3 cols
matrix = [[c for c in range(r, r+C)] for r in range(R)]

for r in range(R):
    for c in range(C):
        print((r,c))


print('\nUsing product():')

for r, c in product(range(R), range(C)):
    print((r,c))

'''
Not super recommended though, especially for interviews. For example, if you need to do
something after each row, you might need to add:
  if c % C == C - 1:
      print('new row')
instead of just adding print('new row') after the inner for loop.
'''
