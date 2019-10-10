'''TESTCASE
4
3 0 6 4
-
2
0 1
-
16
9 6 3 4 5 8 9 1 2 3 1 5 3 1 4 6
-
6
1 9 7 2 3 1
'''
import numpy as np

n = int(input())
np.random.seed(n)

a1 = np.array(list(map(int, input().split())))
a2 = np.zeros(n)
a3 = np.arange(0, n*0.2-0.1, 0.2)
a4 = np.linspace(0, 2, n)
a5 = 1 + 2 * np.random.rand(n)

a = a1 + a2 + a3 + a4 + a5
a = a.reshape((2, n//2))

print('ndim: {}, shape: {}, size: {}, itemsize: {}, dtype: {}'.format(
    a.ndim, a.shape, a.size, a.itemsize, a.dtype))
print(a)
