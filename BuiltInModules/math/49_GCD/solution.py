'''TESTCASE
4 6
-
123 4961
-
214134 13214
-
324325 30850
'''
import math
a, b = map(int, input().split())
print(math.gcd(a, b))