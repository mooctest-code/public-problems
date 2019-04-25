#all
studentNum = int(input())
res = []
for i in range(studentNum):
    studentList = list(input().split(','))
    if(all(studentList)):
        res.append(studentList)
print(res)