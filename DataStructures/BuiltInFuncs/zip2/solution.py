'''TESTCASE
grandgrandfather,grandfather,father,son,grandson
-
a,b,c,d,e,f
-
1,2,3,4,5,6,7,8,9,7,8,9,4,5,6,1,2,3
'''
#zip2
str1 = list(input().split(','))
zipped = zip(str1[:-1],str1[1:])
for i in zipped:
    print(i)