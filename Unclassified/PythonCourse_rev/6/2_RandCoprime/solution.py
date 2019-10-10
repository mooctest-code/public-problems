'''TESTCASE
0
-
10
-
100
-
10
'''
import random
import math

random.seed(int(input()))

a = random.randint(1, 100)
b = random.randint(1, 100)
t = '' if math.gcd(a, b) == 1 else 'n\'t'
print('{} and {} are{} coprime'.format(a, b, t))
