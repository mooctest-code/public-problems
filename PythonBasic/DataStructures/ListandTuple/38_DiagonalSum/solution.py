'''TESTCASE
3
1 2 3
4 5 6
7 8 9
-
2
1 2
2 1
-
5
9 8 7 6 5
4 3 2 1 0
1 2 3 4 5
6 7 8 9 0
1 3 5 7 9
'''
n = int(input())
s = 0
for i in range(n):
    a = list(map(int, input().split()))
    s += a[i]
print(s)