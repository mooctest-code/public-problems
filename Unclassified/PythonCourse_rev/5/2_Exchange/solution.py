'''TESTCASE
10.0USD
-
100EUR
-
100CNY
-
100BTC
'''
l = input()
c = 6.91
r = 0
u = 'USD'
if l[-3:] == 'USD':
    r = float(l[:-3]) * c
    u = 'CNY'
elif l[-3:] == 'CNY':
    r = float(l[:-3]) / c

print('{} is {:.2f}{}'.format(l, r, u) if r
      else 'Invalid input.')
