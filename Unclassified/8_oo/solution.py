'''TESTCASE
2
'Tom',63;'Allen',85;'Toney',83
'Eve',74;'Adan',97;'Julia',80
'''
class Register:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, tup):
        self.scores.append(tup)

    def gte80(self):
        g = []
        for stu in self.scores:
            if stu[1] >= 80:
                g.append(stu[0])
        return g    

class Teacher:
    def __init__(self):
        self.registers = []

    def add_register(self, reg):
        self.registers.append(reg)

    def gte80(self):
        g = []
        for r in self.registers:
            g.extend(r.gte80())
        return g

cnt = int(input())

xiaonan = Teacher()
for i in range(cnt):
    l = input().split(';')
    reg = Register(i)
    for j in l:
        pair = j.split(',')
        reg.add_score((eval(pair[0]), int(pair[1])))
    xiaonan.add_register(reg)

print(xiaonan.gte80())
