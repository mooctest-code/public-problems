'''TESTCASE
100
-
1000
-
10000
-
1234
-
10
'''
from scipy import stats

n = int(input())
e = stats.expon.cdf(n, scale=1000)
print('{:.6f}'.format(1-e))
