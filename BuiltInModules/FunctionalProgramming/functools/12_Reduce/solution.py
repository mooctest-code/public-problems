'''TESTCASE
[1, 3, 7]
-
['a', 'c', 'e']
-
[[1], [2], [3]]
'''
from functools import reduce
print(reduce(lambda x,y: x+y, eval(input())))