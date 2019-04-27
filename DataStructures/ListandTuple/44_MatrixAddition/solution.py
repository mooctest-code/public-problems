'''TESTCASE
2
1 2
2 1
2 1
1 2
-
3
1 2 3
3 2 1
1 2 3
3 3 3
1 1 1
-1 -1 -1
'''
def getMatrix(n):
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    return a

n = int(input())
a1 = getMatrix(n)
a2 = getMatrix(n)

for i in range(n):
    print(' '.join(map(str, [a1[i][j] + a2[i][j] for j in range(n)])))