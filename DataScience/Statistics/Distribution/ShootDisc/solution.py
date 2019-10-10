'''TESTCASE
1
-
2
-
3
-
4
-
5
'''
r = int(input())
k = 1 / (r * r)
print('{:.4f}'.format(k))
e = 2 / 3 * r
print('{:.4f}'.format(e))
print('{:.4f}'.format(r**2/2 - e**2))
