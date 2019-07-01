'''TESTCASE
6 4
-
123 82
-
36 78
-
10 10
'''


def gcd(a: int, b: int):
    return gcd(b, a % b) if b else a


a, b = map(int, input().split())
print(gcd(a, b))
