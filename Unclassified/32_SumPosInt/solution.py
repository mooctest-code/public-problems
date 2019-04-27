'''TESTCASE
4
-
5
-
9
-
12
-
14
-
23
-
37
-
46
-
99
'''
n = int(input())

f = [[0 for j in range(n+1)] for i in range(n+1)]
f[0][0] = 1

# use j part to divide i
for i in range(0, n+1):
    for j in range(0, i+1):
        if i == 1:
            f[i][1] = 1
        else: # i = i - 1 + 1 or i - j + j
            f[i][j] = f[i-1][j-1] + f[i-j][j]
            
print(sum(f[n]))

# def _sum(a, b):
#     if a >= 2*b:
#         return _sum(a-b, b) + _sum(a, b+1)
#     else: return 1 if a >= b else 0

# print(_sum(n, 1))