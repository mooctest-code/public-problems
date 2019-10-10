'''TESTCASE
[1, 2]
(1, 2, 3)
{1: 2}
'1'
-
['1', 2]
('1', 2)
{'1': 2}
1.2
'''
inp = [eval(input()) for i in range(4)]
for i in range(4):
    print(inp[i])
print(inp)