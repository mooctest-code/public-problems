'''TESTCASE
NJU_
['Liuyun', 'Xuxu', 'Yangjun', 'Jiangchen']
-
NJUSE_
['Liuyun', 'Xuxu', 'Yangjun', 'Xiaoming']
-
English~
['Hanmeimei', 'Xiaoming', 'Lilei']
'''
p = input()
l = eval(input())

print(['{} {}{}'.format(i, p, l[i]) for i in range(len(l))])