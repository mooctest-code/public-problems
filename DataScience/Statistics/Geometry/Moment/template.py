def A(k: int, x):
    return  # TODO return Ak


def B(k: int, x):
    return  # TODO return Bk


x = list(map(float, input().split()))
for k in range(1, 5):
    print('{:.4f} {:.4f}'.format(A(k, x), B(k, x)))
