'''TESTCASE
0,10
-
-1,20
'''

ls=[1,2,3]
ind,num=map(int,input().split(','))
ls.insert(ind,num)
print(ls)