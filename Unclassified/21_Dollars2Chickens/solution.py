'''TESTCASE
12
-
56
-
178
-
1000
-
999999
'''
n = int(input())

max_g = n // 5

cnt = 0
for g in range(0, max_g+1):
    if n-7*g < 0 or (n - 7 * g) % 4:
        continue
    cnt += 1

print(cnt)