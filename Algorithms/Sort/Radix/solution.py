'''TESTCASE
3 4 5 2 1
-
0 9 1 0 19 9 0 15 19 17
-
2 6 3 9 4 6 5 2 0 8
-
-2 1 -1 -3 9 -5 3 -4 5 -8
'''

def radix(a):
    _min = min(a)
    a = list(map(lambda x: x - _min, a))
    bits = len(str(max(a)))
    base = 1
    buckets = [[] for i in range(10)]
    while bits:
        for x in a:
            buckets[x // base % 10].append(x)
        a = []
        for i in range(10):
            a += buckets[i]
            buckets[i] = []
        base *= 10
        bits -= 1
    return list(map(lambda x: x + _min, a))

a = list(map(int, input().split()))
print(*radix(a))
