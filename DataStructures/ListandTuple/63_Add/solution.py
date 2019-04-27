'''TESTCASE
6
3 5 0 0 2 5
-
7
2 7 11 15 1 8 7
-
20
3 4 6 8 2 6 7 2 7 6 3 7 6 0 0 6 3 0 3 6
-
49
1 7 5 5 8 0 0 6 1 3 9 2 8 8 7 2 3 3 9 8 4 2 9 4 8 7 4 7 0 0 0 7 4 4 1 7 2 0 0 7 8 2 3 3 7 5 0 2 6
'''
n = int(input())
l = list(map(int, input().split()))

cnt = 0
for i in range(len(l)):
    for j in range(i):
        if l[i] + l[j] == 9:
            cnt += 1

print(cnt)