'''TESTCASE
3
abc def ghi
3 2 1
-
4
ab cd ef gh
3 2 1 0
'''
n = int(input())
a = input().split()
b = [int(i) for i in input().split()]

for i in range(n):
    print('{}: {}'.format(a[i], b[i]))