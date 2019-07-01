'''TESTCASE
4.2
-
7.6 2.6 3.2 4.4 5.4 6.8 8.8
-
4.53 2.68 6.55 6.12 8.31 7.12 8.00 9.61 7.66 5.47 7.85 7.43 7.64 5.89 7.06 1.22 9.71 6.86 6.19 6.86
-
11.34 6.46 1.50 3.53 6.52 6.69 5.09 7.46 4.67 6.77 5.10 6.68 6.24 2.23 5.38 9.55
'''

import numpy as np
from scipy import stats

a = np.array(list(map(float, input().split())))
mode = stats.binned_statistic(
    a, a, statistic='count', bins=[i*3 for i in range(0, int(a.max())//3+2)]).statistic
maxcnt = mode.max()
for i in range(mode.size):
    if mode[i] == maxcnt:
        print('[{}, {})'.format(i*3, (i+1)*3))
