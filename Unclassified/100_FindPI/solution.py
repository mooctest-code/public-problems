'''TESTCASE
None
'''
a = 1
s = 1
pi = 0

while 1/a > 1e-6:
    pi += 4 / a * s
    a += 2
    s *= -1

print('{:.8f}'.format(pi))