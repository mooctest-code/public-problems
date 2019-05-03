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

def bubble(a: list):
    l = len(a)
    for i in range(l):
        for j in range(i+1, l):
            if a[j] < a[i]:
                swap(a, i, j)

a = list(map(int, input().split()))
bubble(a)
print(*a)
