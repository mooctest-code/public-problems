'''TESTCASE
2
-
12
'''

ls=[1,2,3,4,5,6,7,8,9]
n=int(input())
if n in ls:
	ls.remove(n)
	print(ls)
else:
	print('Error! The number %d is not in ls!'%n)