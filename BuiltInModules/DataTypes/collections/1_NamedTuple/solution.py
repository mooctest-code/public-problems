'''TESTCASE
1 2
-
3 4
-
-1 -2
'''
from collections import namedtuple

Point = namedtuple('Point', 'x y')

print(Point._make(map(int, input().split())))