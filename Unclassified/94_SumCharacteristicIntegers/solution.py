'''TESTCASE
1 100
-
324 56545
-
32454 45356
-
123 456
'''
a = list(map(int, input().split()))

cnt = 0
for i in range(a[0], a[1]+1):
    if i % 3 == 1 and i % 5 == 3:
        cnt += i

print(cnt)