'''TESTCASE
60 160
-
40 170
-
120 160
-
90 180
'''
a = list(map(int, input().split()))

b = a[0]/((a[1]/100)**2)

l = [18.5, 24, 28]
s = ['too thin', 'normal', 'overweight', 'fat']

i = 0
while i < 3 and b > l[i]:
    i += 1

print('Your BMI is {:.1f}, {}'.format(b, s[i]))