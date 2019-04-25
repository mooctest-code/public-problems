class Complex(complex):
    def __init__(self, real, imag):
        complex.__init__(real, imag)

    def __repr__(self):
        return '{} + {}j'.format(super().real, super().imag)

    def __str__(self):
        return 'Complex(real={}, imag={})'.format(super().real, super().imag)

real, imag = map(int, input().split())
comp = Complex(real, imag)
print(repr(comp))
print(str(comp))
print(comp)
