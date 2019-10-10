'''TESTCASE
xiaoming xiaoli xiaohua
-
xiaoli xiaohua xiaohuang xiaochen
-
xiaoliu xiaozhang xiaocong
-
xiaoming xiaoliu xiaozhang xiaochen xiaoli
'''
a: list = input().split()
c = 'xiaochen'
m = 'xiaoma'

if c in a:
    a.remove(c)

a.insert(0, c)
a.append(m)

print(*a)
