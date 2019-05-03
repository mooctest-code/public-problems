'''TESTCASE
100 10
-
43278 8
-
4324 8
-
12345 6
'''
n, m = map(int, input().split())

d = n
while m > 1:
    d += n
    n /= 2
    m -= 1

print(d, n)