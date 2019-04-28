'''TESTCASE
0
-
3
-
4
-
1
'''

class A:
    def __init__(self):
        self.n = 1

    def add(self, m):
        self.n += m


class B(A):
    def __init__(self):
        self.n = 2

    def add(self, m):
        # super().add(m)
        self.n += m

class C(A):
    def __init__(self):
        self.n = 2

    def add(self, m):
        super().add(m)
        self.n += m

class D(B, C):
    def __init__(self):
        self.n = 3

    def add(self, m):
        super().add(m)
        self.n += m

d = D()
d.add(int(input()))
print(d.n)