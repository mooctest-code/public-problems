m, n = map(int, input().split())

An = [[0 for x in range(n+1)] for x in range(m+1)]
An[0][0] = 1
for i in range(n+1):
    for j in range(1,m+1):
        if i > j:
            An[j][i] == 0
        else:
            An[j][i] = An[j-1][i] + An[j][i-1]
print(An[m][n])