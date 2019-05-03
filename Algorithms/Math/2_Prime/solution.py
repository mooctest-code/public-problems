'''TESTCASE
1
-
2
-
13
-
234231
-
9834283
-
4294967291
'''
import math

def is_prime(a):
    if a < 2: return False
    if a % 2 == 0: return True
    r = math.floor(math.sqrt(a))
    for i in range(3, r, 2):
        if a % i == 0:
            return False
    return True

a = int(input())
print('Yes' if is_prime(a) else 'No')