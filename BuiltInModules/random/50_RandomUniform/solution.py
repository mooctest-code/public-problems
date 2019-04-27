'''TESTCASE
0
-
1
-
2019
'''
import random

a = int(input())
random.seed(a)
print('{:.3f}'.format(random.uniform(10, 20)))