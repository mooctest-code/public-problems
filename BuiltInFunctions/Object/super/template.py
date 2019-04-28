class A:
    def __init__(self):
        self.n = 1

    def add(self, m):
        # TODO

class B(A):
    def __init__(self):
        self.n = 2

    def add(self, m):
        # TODO

class C(A):
    def __init__(self):
        self.n = 2

    def add(self, m):
        # TODO

class D(B, C):
    def __init__(self):
        self.n = 3

    def add(self, m):
        super().add(m)
        self.n += m

d = D()
d.add(int(input()))
print(d.n)