def mixedMoment(data, k: int, l: int):
    return  # TODO


def mixedCentralMoment(data, k: int, l: int):
    return  # TODO


x = map(float, input().split())
y = map(float, input().split())

points = list(zip(x, y))

while True:
    try:
        k, l = map(int, input().split())
        print('{:.4f} {:.4f}'.format(
            mixedMoment(points, k, l),
            mixedCentralMoment(points, k, l)))
    except EOFError:
        break
