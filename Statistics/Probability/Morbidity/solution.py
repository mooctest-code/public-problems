'''TESTCASE
0.001 0.99 0.05
-
0.001 0.99 0.0001
-
0.001 0.99 0.001
-
0.0001 0.95 0.05
-
0.001 1.0 0.1
'''

x, a, e = map(float, input().split())

p = x*a / (x*a + (1-x)*e)

print('{:.6f}'.format(p))

p = x*(1-a) / (x*(1-a) + (1-x)*(1-e))

print('{:.6f}'.format(p))
