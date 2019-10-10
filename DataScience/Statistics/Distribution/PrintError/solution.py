'''TESTCASE
0.001 1000
-
0.001 100
-
0.04 100
-
0.004 362
-
0.0001 100000
'''
from scipy import stats

inp = input().split()
p, n = float(inp[0]), int(inp[1])

bi = stats.binom(n, p)
print('{:.6f}'.format(bi.cdf(2)))

po = stats.poisson(n*p)
print('{:.6f}'.format(po.cdf(2)))
