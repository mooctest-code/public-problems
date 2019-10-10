'''TESTCASE
27 3
-
16 2
'''
a, n = map(int, input().split())

print(round(a**(1/n), 2))