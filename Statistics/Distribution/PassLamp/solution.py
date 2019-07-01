'''TESTCASE
4 0.5
-
5 0.5
-
4 0.8
-
1 0.2
'''


def E(X):
    return sum(map(lambda x: x[0]*x[1], X))


def V(X):
    X2 = ((x[0]*x[0], x[1]) for x in X)
    return E(X2) - E(X) ** 2


inp = input().split()
n, p = int(inp[0]), float(inp[1])

X = tuple(zip((i for i in range(n+1)),
              ((1-p)**i * (p if i < n else 1)
               for i in range(n+1))))

print('X', *(x[0] for x in X), sep='\t')
print('P', *('{:.4f}'.format(x[1])
             for x in X), sep='\t')
print('{:.4f}'.format(E(X)))
print('{:.4f}'.format(V(X)))
