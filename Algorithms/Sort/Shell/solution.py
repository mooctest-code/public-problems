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

def shell(a: list):
    l = len(a)
    step = l // 2
    while step:
        for i in range(step, l):
            while i - step > -1 and a[i] < a[i-step]:
                swap(a, i, i-step)
                i -= step
        step //= 2

a = list(map(int, input().split()))
shell(a)
print(*a)
