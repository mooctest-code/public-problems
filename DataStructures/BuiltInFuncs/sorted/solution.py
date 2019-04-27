'''TESTCASE
xiaoming xiaowang xiaoqiang
579 626 635
23 25 24
-
xluna qiaokeli tang
618 627 684
25 24 23
'''
#sorted
name = list(input().split())
grade = list(map(int,input().split()))
years = list(map(int,input().split()))
# name = ['d','b','c']
# grade = [10,15,20]
# years = [25,20,15]
students= zip(name,grade,years)

sortA = sorted(students, key=lambda s: s[1])
print(sortA)
students= zip(name,grade,years)
sortB = sorted(students, key=lambda s: s[2])
print(sortB)