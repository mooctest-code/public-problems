'''TESTCASE
4
'Tom',63;'Allen',85
'Adan',97;'Julia',80
'Eve',74;'Toney',55
'Jeff',82;'Jerry',99
'''
def assignLesson(a):
    for c in a:
        s = 0
        for i in c:
            s += i[1]
        avg = s / len(i)

        yield 'Normal' if avg < 80 else 'Hard'

cnt = int(input())

a = []
for i in range(cnt):
    l = input().split(';')
    r = []
    for j in l:
        pair = j.split(',')
        r.append((eval(pair[0]), int(pair[1])))
    a.append(r)

for i in assignLesson(a):
    print(i)