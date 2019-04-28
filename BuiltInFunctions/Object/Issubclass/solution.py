'''TESTCASE
B
-
C
'''
class A:
    pass
class B(A):
    pass
class C():
    pass
name = input()
print(issubclass(eval(name),A))
