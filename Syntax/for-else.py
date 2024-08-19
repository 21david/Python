'''
You can put an else after a for loop. It will run only if the for loop completes fully.
If the for loop breaks at some point, it will skip the else block completely.

Another way to think of it is "if-for-fully-completes: [code]"

It can also be used with while and try. See the other files in this folder.
'''

for i in range(10):
    print(i)
else:
    print('done')
'''
Output:
0
1
2
3
4
5
6
7
8
9
done
'''


for i in range(10):
    print(i)
    if i == 5:
        break
else:
    print('done')
'''
Output:
0
1
2
3
4
5
'''
