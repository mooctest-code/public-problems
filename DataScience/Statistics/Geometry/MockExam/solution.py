'''TESTCASE
78 74 60 42 53 63 70 90 54 82
85 69 76 53 70 59 82 95 60 67
-
60 42 53 68 70 90 54 82
59 82 95 60 87 70 53 70
-
60 42 93 68 70 90 54 82
90 53 70 59 62 55 60 87
-
45 70 33 75 70 56 74 7 99 24
50 39 84 95 44 55 8 70 92 2
'''


def mixedMoment(data, k: int, l: int):
    return sum(map(lambda d: (d[0]**k)*(d[1]**l), data)) / len(data)


def mixedCentralMoment(data, k: int, l: int):
    x, y = zip(*data)
    avgx = sum(x) / len(data)
    avgy = sum(y) / len(data)
    _data = list(map(lambda d: (d[0]-avgx, d[1]-avgy), data))
    return mixedMoment(_data, k, l)


def std(data):
    l = len(data)
    avg = sum(data) / l
    d = sum(map(lambda x: (x-avg)**2, data))
    return (d / l) ** 0.5


a = list(map(int, input().split()))
b = list(map(int, input().split()))

cov = mixedCentralMoment(list(zip(a, b)), 1, 1)
rel = cov / (std(a) * std(b))

print('{:.4f} {:.4f}'.format(cov, rel))
