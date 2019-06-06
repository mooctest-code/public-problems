class Complex(complex):
    def __init__(self, real, imag):
        complex.__init__(real, imag)

    def __repr__(self):
        return # TODO

    def __str__(self):
        return # TODO

real, imag = map(int, input().split())
comp = Complex(real, imag)
print(repr(comp))
print(str(comp))
print(comp)
