'''TESTCASE
5
1 3 5 4 6
-
4
4 1 2 3
-
14
1 2 3 4 5 6 7 6 7 5 4 3 2 1
-
1
1
'''
n = int(input())
l = list(map(int, input().split()))
l.sort()
a = len(l)
print(int(l[a//2]) if a & 1 else int((l[a//2-1]+l[a//2])/2))