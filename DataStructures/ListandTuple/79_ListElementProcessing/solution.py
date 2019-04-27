'''TESTCASE
[1, 4, 5, 7, 2, 3]
(3, 4)
4
-
[9, 3, 5, 2, 3, 5, 1, 6, 3, 2]
(2, 1)
5
'''
l = eval(input())
t = eval(input())
n = int(input())

l[t[0]] = t[1]

print(list(filter(lambda x: x != n, l)))