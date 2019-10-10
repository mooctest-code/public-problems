'''TESTCASE
bin1,bin2,bin3
com1,com2,com3,com4,com5
-
bin1,bin2,bin3,bin4,bin5
com1,com2,com3
-
bin1,bin2,bin3,bin4,bin5
com1,com2,com3,com4,com5
'''
#zip
str1 = list(input().split(','))
str2 = list(input().split(','))
zipped = zip(str1,str2)
for i in zipped:
    print(i)