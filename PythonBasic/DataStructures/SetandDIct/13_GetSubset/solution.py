'''TESTCASE
{1}
{2, 3}
-
{1}
{1}
-
{1, 2, 3}
{2, 3, 4}
'''
set1 = eval(input())
set2 = eval(input())

print(set1.issubset(set2))