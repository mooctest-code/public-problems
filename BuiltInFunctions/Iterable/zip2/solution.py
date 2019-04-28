'''TESTCASE
[('bin1', 'com1'), ('bin2', 'com2'), ('bin3', 'com3')]
-
[('bin1', 'com1'), ('bin2', 'com2'), ('bin3', 'com3'), ('bin4', 'com4'), ('bin5', 'com5')]
'''
ts = list(zip(*eval(input())))
print(list(ts[0]))
print(list(ts[1]))