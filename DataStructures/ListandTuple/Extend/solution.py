'''TESTCASE
9,8,7,6
-
1,2,3,4,5
'''

ls=[1,2,3]
n=list(map(int,input().split(',')))
ls.extend(n)
print(ls)