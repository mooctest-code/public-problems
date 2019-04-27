'''TESTCASE
16
4
5
3
'''
[a, b, c, d] = [int(input()) for i in range(4)]

print(a/b)
[div, mod] = divmod(a, b)
print(div)
print(mod)
print(c**d)