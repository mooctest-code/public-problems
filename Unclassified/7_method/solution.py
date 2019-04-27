'''TESTCASE
[('Tom', 63), ('Allen', 85), ('Adan', 97), ('Adam', 80), ('Eve', 74), ('Toney', 55), ('Jerry', 84)]
'''
l = eval(input())

n = []

for i in l:
    if i[1] >= 80:
        n.append(i[0])

print(n)