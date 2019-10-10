'''TESTCASE
1000
-
100000
-
300000
-
456789
'''

import random

random.seed(0)

n = int(input())

cnt = 0
for i in range(n):
    x = random.random()
    y = random.random()

    if x*x + y*y < 1:
        cnt += 1

print('{:.4f}'.format(cnt*4/n))
