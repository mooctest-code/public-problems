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

def counting(a: list):
    _min, _max = min(a), max(a)
    buckets = [0] * (_max - _min + 1)
    for x in a:
        buckets[x-_min] += 1
    a = []
    for i in range(len(buckets)):
        if buckets[i]:
            a += [i+_min] * buckets[i]
    return a

a = list(map(int, input().split()))
print(*counting(a))
