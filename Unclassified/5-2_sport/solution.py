'''TESTCASE
'Tom'
'110M'
13.9
'Eve'
'800M'
'4min'
'Allen'
'110M'
14.2
'''
l = []
for i in range(3):
    [n, p, r] = [eval(input()) for j in range(3)]
    if p == '110M':
        l.append((n, r))

print(l)