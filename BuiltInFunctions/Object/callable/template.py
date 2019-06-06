class A:
    def __init__(self, message):
        self.message = message
    
    # TODO

a = A(input())

print(callable(A))
print(callable(a))
a()