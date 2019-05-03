'''TESTCASE
3 4 5 2 1
-
0 9 1 0 19 9 0 15 19 17
-
2 6 3 9 4 6 5 2 0 8
-
-2 1 -1 -3 9 -5 3 -4 5 -8
'''

def swap(a: list, i: int, j: int):
    a[i], a[j] = a[j], a[i]

def insertion(a: list):
    l = len(a)
    for i in range(1, l):
        x, p = a[i], i - 1
        while p > -1 and x < a[p]:
            a[p+1] = a[p]
            p -= 1
        a[p+1] = x

def bucket(a: list):
    _min, _max = min(a), max(a)
    n = 5
    buckets = [[] for i in range((_max-_min) // n + 1)]
    for x in a:
        buckets[(x-_min)//n].append(x)
    a = []
    for bucket in buckets:
        insertion(bucket)
        a += bucket
    return a

a = list(map(int, input().split()))
a = bucket(a)
print(*a)
