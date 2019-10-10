'''TESTCASE
13
-
40
-
123
-
0
-
2
-
123456
-
1234567890123456
'''
a = int(input())

n = 0
cnt = 0
while n < a:
    n = n + pow(3, cnt)
    cnt = cnt + 1

print(cnt)
