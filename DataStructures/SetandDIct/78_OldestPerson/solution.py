'''TESTCASE
{'Cong': 22, 'Ming': 54, 'Mei': 21}
-
{'Li': 23, 'Han': 43, 'Lei': 19}
'''
d = eval(input())

maxkv = ('', 0)
for k, v in d.items():
    if v > maxkv[1]:
        maxkv = (k, v)

print(maxkv[0])