'''TESTCASE
abc def hij
-
1 2 3 4
-
aaa bbb ccc ddd
-
a b c
'''


def print_each_to_line(*args):
    for arg in args:
        print(arg)


print_each_to_line(input().split())
