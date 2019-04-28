'''TESTCASE
3
xiaowang,78,89,45,26
xiaogang,12,,45,78
xluna,98,89,89,94
-
2
zhangqiang,60,76,98,96
yini,78,25,,94
-
4
MLXG,15,78,56,48
mage,78,90,65,88
emmmm,45,,12,17
paohui,47,58,45,
'''
studentNum = int(input())
res = []
for i in range(studentNum):
    studentList = list(input().split(','))
    if any(map(lambda x: int(x) < 60 if x != '' else True, studentList[1:])):
        res.append(studentList[0])
print(res)