'''TESTCASE
7423986540924719 3
-
32985716817197 5
-
10203040506 6
-
45741986417248091 6
'''

from functools import reduce


def mul(x): return reduce(int.__mul__, x, 1)


a, n = input().split()
n = int(n)
a = list(map(int, a))
mp, mi = 0, 0
i = 0
while i+n < len(a):
    try:
        i = a.index(0, i, i+n) + 1
    except ValueError:
        p = mul(a[i:i+n])
        if p > mp:
            mp = p
            mi = i
        i += 1


print(''.join(map(str, a[mi:mi+n])))
print(mp)
