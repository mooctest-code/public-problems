'''TESTCASE
15 3
-
25 12
-
43 21
-
12 34
'''
x, y = map(int, input().split())

print('{} + {} = {}'.format(x, y, x+y))
print('{} - {} = {}'.format(x, y, x-y))
print('{} * {} = {}'.format(x, y, x*y))
print('{} / {} = {:.2f}'.format(x, y, x/y))
print('{} // {} = {}'.format(x, y, x//y))
