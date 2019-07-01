'''TESTCASE
4 2
-
2 3
-
3 7
-
2 2
-
1 1
'''

n, m = map(int, input().split())

t = n + m
d = t * (t-1)

p00 = m * (m-1) / d
p01 = m * n / d
p10 = n * m / d
p11 = n * (n-1) / d

print('X\\Y\t0\t1')
print('0\t{:.4f}\t{:.4f}'.format(p00, p01))
print('1\t{:.4f}\t{:.4f}'.format(p10, p11))
