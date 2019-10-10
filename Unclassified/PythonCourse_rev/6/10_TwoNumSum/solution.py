'''TESTCASE
1 4 5 6 9 11 15 19 29
15
-
5 8 17 19 34 67 89
30
-
1 2 3 4 5 6 7 8 9 10
9
-
-9 -8 -7 -4 5 6 8 9
10
-
-9 -8 -7 -4 5 6 8 9
1
'''


def twonumSum(l: list, n: int):
    i, j = 0, len(l)-1
    while i < j:
        s = l[i] + l[j]
        if s < n:
            i += 1
        elif s > n:
            j -= 1
        else:
            return (i, j)
    return None


l = list(map(int, input().split()))
n = int(input())

twonum = twonumSum(l, n)
print(*twonum) if twonum else print('Not Found')
