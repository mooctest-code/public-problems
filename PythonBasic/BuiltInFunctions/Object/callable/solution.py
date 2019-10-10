'''TESTCASE
A
-
B
'''

class A:
    def __init__(self, message):
        self.message = message
    
    def __call__(self):
        print(self.message)

a = A(input())

print(callable(A))
print(callable(a))
a()