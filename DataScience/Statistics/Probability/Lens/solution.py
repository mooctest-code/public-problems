'''TESTCASE
1
-
2
-
3
-
5
-
7
'''


def P(i):
    return min(0.4 + 0.1 * i, 1.0)


n = int(input())
p = 1
for i in range(1, n+1):
    p *= (1-P(i))

print('{:.4f}'.format(p))
