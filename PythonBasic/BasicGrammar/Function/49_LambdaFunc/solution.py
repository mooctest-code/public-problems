'''TESTCASE
10
20
-
0
-1
'''
MAX = lambda x, y: x if x > y else y
MIN = lambda x, y: x if x < y else y

a = int(input())
b = int(input())

print(MAX(a, b))
print(MIN(a, b))
