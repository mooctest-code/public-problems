'''TESTCASE
1
-
3
-
2
-
4
-
5
'''
from scipy import stats
n = int(input())
bi = stats.binom(n, 0.5)
print(*('{:.4f}'.format(bi.pmf(i)) for i in range(n+1)))
