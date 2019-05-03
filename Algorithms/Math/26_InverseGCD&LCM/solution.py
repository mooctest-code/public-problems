'''TESTCASE
4 60
-
2 228
-
28 392
-
16 2304
-
193 11580
-
128 768
'''
import math

[gcd, lcm] = list(map(int, input().split()))

k = 1
m = 0
ans = (0, 0)
for k in range(1, lcm//gcd):
    n1 = k * gcd # num1
    if lcm % n1: # check num1
        continue
    [n2, m] = divmod(lcm, k) # num2
    if n2 <= n1 or math.gcd(n1, n2) != gcd: break
    if m or n2 % gcd: 
        continue
    if n1 + n2 >= m:
        m = n1 + n2
        ans = (n1, n2)

print('{} {}'.format(ans[0], ans[1]))
