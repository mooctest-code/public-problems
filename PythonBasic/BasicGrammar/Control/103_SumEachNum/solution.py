'''TESTCASE
80
-
120
-
400
'''
n = int(input())

cnt = 0
for i in range(1, n+1):
    x = i
    s = 0
    while x:
        s += x % 10
        x //= 10
    if s % 5 == 0:
        cnt += 1

print(cnt)