'''TESTCASE
{1, 2, 3}
{2, 3, 4}
-
{1}
{0}
-
{1, 2, 3}
{0, 1, 2}
'''
set1 = eval(input())
set2 = eval(input())

print(set1.difference(set2))