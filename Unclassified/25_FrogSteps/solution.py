'''TESTCASE
2
-
5
-
13
-
19
-
0
'''
n = int(input())

f1, f2 = 1, 2

if n == 0: 
    f1 = 0

while n > 1:
    n -= 1
    f1, f2 = f2, f1+f2

print(f1)