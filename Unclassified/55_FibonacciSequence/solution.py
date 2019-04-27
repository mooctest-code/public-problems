'''TESTCASE
1
-
3
-
14
-
23
-
34
'''
n = int(input())

f1, f2 = 1, 1
while n > 1:
    f1, f2 = f2, f1+f2
    n -= 1

print(f1)