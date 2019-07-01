'''TESTCASE
0.1
-
0.01
-
0.001
-
0.0001
'''

import random

random.seed(0)

x = float(input())

p, n = 0, 0
cnt = 0
while True:
    r = random.randint(0, 1)
    if r:
        p += 1
    else:
        n += 1

    if abs(p - n) < x * (p+n):
        cnt += 1
    else:
        cnt = 0

    if cnt == 5:
        break

print(p+n)
