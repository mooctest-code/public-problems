'''TESTCASE
0.02 0.015 0.01
-
0.03 0.01 0.005
-
0.01 0.01 0.01
-
0.3 0.04 0.01
'''

a = list(map(float, input().split()))
a.append(1-sum(a))

p = 0
for k, v in zip(a, (0.15, 0.1, 0.05, 0.5)):
    p += k * v

print('{:.4f}'.format(p))
