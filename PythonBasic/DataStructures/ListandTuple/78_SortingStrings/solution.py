'''TESTCASE
java,c,python
-
i,love,coding
-
hello,world
'''
a = input()
l = a.split(',')
l.sort()
print(','.join(l))