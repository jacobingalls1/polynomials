from fraction import Fraction

class Polynomial():
    def __init__(self, seed):
        if type(seed) in [int, float, Fraction]:
            self.coeff = [seed]
        elif type(seed) in [list, tuple]:
            self.coeff = seed
        else:
            raise Exception('Cannot cast type %s as Fraction'%type(num))

    def __mul__(self, b):#lists of coefficients
        if type(b) is not Polynomial:
            b = Polynomial(b)
        a = self.coeff
        b = b.coeff
        ret = [0 for i in range(len(a)+len(b)-1)]
        for i in range(len(a)):
            for j in range(len(b)):
                ret[i+j]+=a[i]*b[j]
        return Polynomial(ret)

    __rmul__=__mul__

    def __add__(self,b):
        if type(b) is not Polynomial:
            b = Polynomial(b)
        a = self.coeff
        b = b.coeff
        ret = [0 for i in range(max(len(a), len(b)))]
        for i in range(len(ret)):
            if i<len(a):
                ret[i] += a[i]
            if i<len(b):
                ret[i] += b[i]
        return Polynomial(ret)

    __radd__=__add__

    def trim(self):
        while self.coeff[-1] == 0:
            self.coeff = self.coeff[:-1]

    def __str__(self, var='x'):
        ret=''
        for i in range(1, len(self.coeff)):
            if self.coeff[i]:
                if ret:
                    ret = ret + ' + %s*%s^%i'%(self.coeff[i], var, i)
                else:
                    ret = '%s*%s^%i'%(self.coeff[i], var, i)
        return ret

    def solve(self, n):
        poly=self.coeff
        ret=0
        for i in range(len(poly)):
            ret += poly[i] * (n**i)
        return ret 
