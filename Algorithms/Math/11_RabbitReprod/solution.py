'''TESTCASE
4
-
12
-
24
-
37
'''
n = int(input())

f1, f2 = 1, 1
for i in range(n-1):
    f1, f2 = f2, f1+f2

print(f1*2)