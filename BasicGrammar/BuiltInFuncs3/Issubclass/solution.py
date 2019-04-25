class A:
    pass
class B(A):
    pass
class C():
    pass
num = input()
if num == 'B':
    print(issubclass(B,A))
if num == 'C':
    print(issubclass(C,A))
