'''TESTCASE
1 4 2
-
3 4 -2
'''
a, n, d = map(int, input().split())
print(*range(a, a+n*d, d))