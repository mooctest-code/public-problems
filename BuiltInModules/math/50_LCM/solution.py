'''TESTCASE
4 258
-
3265 86435
-
3243 752983
-
123 789
'''
import math
a, b = map(int, input().split())
print(a * b // math.gcd(a, b))