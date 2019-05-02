'''TESTCASE
1
-
3
-
7
-
9
'''
# by @colinshi in http://www.runoob.com/python/python-exercise-example61.html

def sj():
    a = [1]
    while True:
        yield a
        a = [sum(i) for i in zip([0] + a, a + [0])]

n = int(input())
for x in sj():
    print(' '.join(map(str, x)))
    n -= 1
    if not n:
        break