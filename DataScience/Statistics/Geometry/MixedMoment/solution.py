'''TESTCASE
8.82 7.96 7.13 5.15 0.9
8.09 2.6 9.48 0.0 9.89
1 1
1 2
2 1
-
3.91 3.54 5.25 8.32 2.98 2.63 6.4 8.59
3.11 9.49 8.35 7.34 2.02 6.63 1.78 2.14
1 1
2 2
-
0.96 9.35 6.28 0.37 9.75 2.92 3.1 4.93 3.1 5.38 0.11 8.18 9.93 6.51 5.09 2.14
1.48 5.5 5.32 8.37 4.82 6.43 7.17 3.19 1.65 2.35 9.59 5.65 7.63 8.21 8.02 4.6
1 1
2 1
2 2
-
1.56 3.58 4.99
6.73 4.92 8.45
1 1
3 3
'''


def mixedMoment(data, k: int, l: int):
    return sum(map(lambda d: (d[0]**k)*(d[1]**l), data)) / len(data)


def mixedCentralMoment(data, k: int, l: int):
    x, y = zip(*data)
    avgx = sum(x) / len(data)
    avgy = sum(y) / len(data)
    _data = list(map(lambda d: (d[0]-avgx, d[1]-avgy), data))
    return mixedMoment(_data, k, l)


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
