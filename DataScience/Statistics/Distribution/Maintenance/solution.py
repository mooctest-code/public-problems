'''TESTCASE
80
-
20
-
100
-
0
-
50
'''

from scipy import stats

n = int(input())

x = stats.binom(n, 0.01)
i = 0
while True:
    if x.cdf(i) > 0.99:
        break
    i += 1

print(i)
