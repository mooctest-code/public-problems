'''TESTCASE
2
-
4
-
7
-
9
'''
a = int(input())

m = 1
for i in range(2, a+1):
    m *= i
print(m)