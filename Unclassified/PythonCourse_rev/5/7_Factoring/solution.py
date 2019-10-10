'''TESTCASE
60
-
17
-
100
-
32
'''


def factoring(a):
    f = []
    i = 2
    while a > 1:
        while a > 1 and a % i == 0:
            f.append(i)
            a //= i
        i += 1
    return f


a = int(input())
print('{}={}'.format(a, '*'.join(map(str, factoring(a)))))
