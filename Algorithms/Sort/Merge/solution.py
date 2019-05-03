'''TESTCASE
3 4 5 2 1
-
0 9 1 0 19 9 0 15 19 17
-
2 6 3 9 4 6 5 2 0 8
-
-2 1 -1 -3 9 -5 3 -4 5 -8
'''

def merge_sort(a):
    n = len(a)
    i = 1
    while i < n:
        j = 0
        while j+i-1 < n:
            l, m, r = j, j+i-1, j+i*2-1
            if r >= n:
                r = n-1
            merge(a, l, m, r)
            j = r + 1
        i *= 2

def merge(a, l, m, r):
    i, j = l, m+1
    temp = []
    while i <= m and j <= r:
        if a[i] < a[j]:
            temp.append(a[i])
            i += 1
        else:
            temp.append(a[j])
            j += 1
    temp += a[i:m+1]
    temp += a[j:r+1]
    a[l:r+1] = temp

a = list(map(int, input().split()))
merge_sort(a)
print(*a)