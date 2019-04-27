'''TESTCASE
13
13 10 9 2 4 65 34 123 43 65 23 19 87
-
5
5 17 8 12 1
-
9
9 8 7 6 5 4 3 2 1
'''
n = int(input())
l = list(map(int, input().split()))
l.sort()
print(' '.join(map(str, l)))