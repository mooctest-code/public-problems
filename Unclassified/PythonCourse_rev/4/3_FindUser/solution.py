'''TESTCASE
{'xiaohong': 'x1a0h0nG', 'xiaoming': '123456', 'xiaoli': 'liLilI'}
-
{'xiaoming': '123456', 'xiaoli': 'liLilI'}
-
{'xiaohong': '123456', 'xiaoming': '123456', 'xiaoli': 'liLilI'}
-
{'Xiaohong': '123456', 'xiaoming': '123456', 'xiaoli': 'liLilI'}
'''
d: dict = eval(input())

print(d.get('xiaohong', 'not found'))
