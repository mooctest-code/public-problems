def pnorm(X, p):
    return  # TODO


X = list(map(float, input().split()))

p = input()
p = int(p) if p != 'inf' else p

print('{:.4f}'.format(pnorm(X, p)))
