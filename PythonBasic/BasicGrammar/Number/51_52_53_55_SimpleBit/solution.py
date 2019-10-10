'''TESTCASE
1 2
-
123 456
-
-1 -2
-
987654321 123456789
'''
a, b = map(int, input().split())

print(a&b)
print(a|b)
print(a^b)
a = ~a
b = ~b
print(b if a > b else a)