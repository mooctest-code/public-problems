'''TESTCASE
2 4
-
10 3
'''
a, b = map(eval, input().split(' '))
(q, r) = divmod(a, b)
print(q, r)