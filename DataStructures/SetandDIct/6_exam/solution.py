'''TESTCASE
[('Tom', 63), ('Allen', 85), ('Adan', 74), ('Julia', 80), ('Jerry', 74), ('Toney', 55)]
'''
l = eval(input())

m = {}
s = []

g = ['A', 'B', 'C', 'D', 'E']

for i in l:
    m[i[0]] = g[(99-i[1])//10] if i[1] >= 60 else 'E'
    if i[1] >= 80:
        s.append(i[0])
print(m)
print(s)