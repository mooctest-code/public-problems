'''TESTCASE
12 123 13
-
7 12 4 246
-
9 78 23 123 0
-
43 78 2 12 78
'''
from functools import cmp_to_key

def cmp(x, y):
    return int(y+x) - int(x+y)

a = input().split()
a = sorted(a, key=cmp_to_key(cmp))
print(''.join(a))
