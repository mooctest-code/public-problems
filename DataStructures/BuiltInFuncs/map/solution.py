'''TESTCASE
1
1 2 5 4 7 8 9 6
-
2
4 5 7 8 9 5 6 4
123 48 75 98 61 35
'''
#map
num = int(input())
for i in range(num):
    str1 = list(map(int,input().split()))
    print(sum(str1))
    print(max(str1))