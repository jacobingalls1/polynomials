import sys
import math

class Fraction():
    def __init__(self, num=1, den=1):
        if type(num) == int:
            self.num = num
            self.den = den
        else:
            raise Exception('Cannot cast type %s as Fraction'%type(num))

    def simplify(self):
        factor = math.gcd(self.den, self.num)
        self.den //= factor
        self.num //= factor

    def __add__(self, a):
        if type(a) is not Fraction:
            a = Fraction(a)
        den = self.den*a.den
        num = self.den*a.num + a.den*self.num
        return Fraction(num, den)

    __radd__=__add__

    def __mul__(self, a):
        if type(a) is not Fraction:
            a = Fraction(a)
        den = self.den*a.den
        num = self.num*a.num
        return Fraction(num, den)

    __rmul__=__mul__

    def __str__(self):
        self.simplify()
        if self.den == 1:
            return str(self.num)
        return '%i/%i'%(self.num, self.den)

    def float(self):
        return self.num/self.den
    
    def __bool__(self):
        return bool(self.num)

