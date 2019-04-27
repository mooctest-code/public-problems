'''TESTCASE
1 2 3 4
-
9 8 7 6
-
2 3 6 7
'''
from itertools import permutations

a = map(int, input().split(' '))
for i in permutations(a, 3):
    print('{}{}{}'.format(i[0], i[1], i[2]))
