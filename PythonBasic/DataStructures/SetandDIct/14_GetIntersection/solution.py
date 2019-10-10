'''TESTCASE
{1}
{1}
-
{1, 2, 3}
{2, 3, 4}
-
{1}
{0}
'''
set1 = eval(input())
set2 = eval(input())

inter = set1.intersection(set2)

print(inter or None)