'''TESTCASE
3 4 5 2 1
-
0 9 1 0 19 9 0 15 19 17
-
2 6 3 9 4 6 5 2 0 8
-
-2 1 -1 -3 9 -5 3 -4 5 -8
'''

def quick_sort(a, l, r):
    stack = [(l, r)]
    while len(stack) > 0:
        p = stack.pop()
        m = partition(a, p[0], p[1])
        if p[0] < m-1:
            stack.append((p[0], m-1))
        if m+1 < p[1]:
            stack.append((m+1, p[1]))

def partition(a, l, r):
    m = a[l]
    while l < r:
        while l < r and a[r] >= m:
            r -= 1
        a[l] = a[r]
        while l < r and a[l] <= m:
            l += 1
        a[r] = a[l]
    a[l] = m
    return l

a = list(map(int, input().split()))
quick_sort(a, 0, len(a)-1)
print(*a)