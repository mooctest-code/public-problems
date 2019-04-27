'''TESTCASE
9
1 2 3 4 5 6 7 8 8
-
8
4 6 8 2 3 2 2 3
-
11
9 1 8 9 0 3 1 7 6 2 9
-
11
2 8 6 4 8 8 3 2 7 7 6
'''
n = int(input())
a = map(int, input().split())
s = set(a)
z = 0 in s
l = len(s)
print((l-z)*(l-1))
