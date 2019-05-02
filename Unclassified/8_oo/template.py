class Register:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, tup):
        self.scores.append(tup)

    def gte80(self):
        # TODO   
        return

class Teacher:
    def __init__(self):
        self.registers = []

    def add_register(self, reg):
        self.registers.append(reg)

    def gte80(self):
        # TODO
        return

cnt = int(input())

xiaonan = Teacher()
for i in range(cnt):
    l = input().split(';')
    reg = Register(i)
    for j in l:
        pair = j.split(',')
        reg.add_score((str(pair[0]), int(pair[1])))
    xiaonan.add_register(reg)

print(xiaonan.gte80())
