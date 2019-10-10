'''TESTCASE
9 9 8.5 10 7 8 8 9 8 10
9
-
9 8 7 6 7 8 8.5 7.5 8.5 8
8.5
-
9 9.5 7 6 7 8 9 7.5 8.5 8
9.5
-
8 6 7 6.5 7 8 9 8 8 8.5
9
'''
a = list(map(float, input().split()))
score = sum(a) - min(a) - max(a) + float(input())
print('{:.2f}'.format(score / (len(a)+1)))
