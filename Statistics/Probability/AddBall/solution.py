'''TESTCASE
1 2
-
3 5
-
1 0
-
0 1
-
6 4
'''

n, m = map(int, input().split())
t = n + m
print('{:.4f}'.format(
    n/t*(m+1)/(t+1) + m/t*m/(t+1)
))
