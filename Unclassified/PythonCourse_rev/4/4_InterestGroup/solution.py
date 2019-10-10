'''TESTCASE
xiaoming xiaozhang xiaoli xiaoliu
xiaoming xiaoli xiaolin
-
xiaoming xiaozhang xiaoli xiaoliu
xiaoming xiaoli xiaolin xiaocong
-
xiaoming xiaozhang xiaoli xiaoliu
xiaolin
-
xiaolin
xiaolin
'''
a = set(input().split())
b = set(input().split())

both = a.intersection(b)
only = a.symmetric_difference(b)

print(len(both), *sorted(both))
print(len(only), *sorted(only))
