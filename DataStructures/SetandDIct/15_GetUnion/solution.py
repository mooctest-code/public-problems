'''TESTCASE
{1, 2, 3}
{1, 2}
-
{1, 2, 3, 4}
{4, 5}
-
{1}
{}
'''
set1 = eval(input())
set2 = eval(input())

print(set1.union(set2))