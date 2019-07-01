'''TESTCASE
6
1 9 7 2 3 1
-
4
3 0 6 4
-
2
0 1
-
16
9 6 3 4 5 8 9 1 2 3 1 5 3 1 4 6
'''
import numpy as np
n = int(input())
a1 = np.array(list(map(int, input().split()))).reshape((2, n//2))
np.random.seed(n)
a2 = np.random.randint(0, 10, n).reshape((2, n//2))

print('sum: {}, min: {}, max: {}'.format(a1.sum(), a1.min(), a1.max()))
print('a1 + a2:\n', a1+a2)
print('a1 * a2:\n', a1*a2)
print('a1 ** a2:\n', a1**a2)
print('a2.T x a1:\n', a2.T@a1)
