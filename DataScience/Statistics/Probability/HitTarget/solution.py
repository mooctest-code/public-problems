'''TESTCASE
0.5 0.4 0.8 0.6
-
0.3 0.4 0.2
-
0.6 0.4 0.6 0.5 0.3
-
1.0
-
0.0
'''

a = list(map(float, input().split()))
p = 1
for i in a:
    p *= (1-i)
print('{:.4f}'.format(1-p))
