'''TESTCASE
1432
-
1111
-
9876
-
3416
'''
a = input()

while a != '6174' and a != '0000':
    a = ''.join(sorted(a))
    l = a[::-1]
    r = a
    a = str(int(l) - int(r)).zfill(4)
    print('{}-{}={}'.format(l, r, a))
