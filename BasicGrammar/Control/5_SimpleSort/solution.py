'''TESTCASE
2 3 1
-
3 2 1
-
0 0 0
-
-2 3 -1
'''
[a, b, c] = map(int, input().split())

if c < b:
    c, b = b, c
if b < a:
    b, a = a, b
if c < b:
    c, b = b, c

print('{} {} {}'.format(a, b, c))
