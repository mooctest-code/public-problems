'''TESTCASE
500
-
50000
-
500000
-
5000
-
10000
'''
from scipy import stats

n = int(input())

bi = stats.binom(3, 0.02)
pb = bi.pmf(1)

hg = stats.hypergeom(n, n*0.02, 3)
ph = hg.pmf(1)

print('{:.6f}'.format(pb))
print('{:.6f}'.format(ph))
