from polynomial import Polynomial
from fraction import Fraction

def showRows(length, rows):
    values = [[1 for i in range(length)]]

    while len(values)<rows:
        new = [1]
        while len(new)<length:
            new.append(new[-1]+values[-1][len(new)-1])
        values.append(new)


    for i in range(len(values)):
        print('\t'*(rows-i), end='')
        for v in values[i]:
            print(v,end='\t\t')
        print()

def binomnum(n):
    ret = Polynomial(Fraction())
    for i in range(n):
        ret *= Polynomial([-i, 1])
    return ret

def factorial(n):
    if n < 2:
        return 1
    return n*factorial(n-1)

def nchoosem(m):
    num=binomnum(m)
    f = Fraction(1,factorial(m))
    return num*f

def findNext(input):
    ret=Polynomial(0)
    m=0
    diffs = input
    while len(diffs) != 1:
        ndif=[diffs[i+1]-diffs[i] for i in range(len(diffs)-1)]
        ret += nchoosem(m)*Polynomial(diffs[0])
        m+=1
        diffs = ndif
    return ret

def continueSequence(values, more):
    poly = findNext(values)
    print('Solving %s'%poly)
    nextValues = [poly.solve(len(values)+i) for i in range(more)]
    for i in values+nextValues:
        print(i, end='\t')
    print()



power = 5
p = Polynomial([1,1,1,1,1,1])
np = Polynomial([0,0,1,1,1,1,1,1])
d6 = Polynomial([0,1,1,1,1,1,1])
#print('offset number cubes:',p*np)
#print('standard number cubes:',d6*d6)



#continueSequence([i**power - (i-1)**power for i in range(1, 10)], 10)
continueSequence([1,2,3,5,7,11,15,22,30,42,56], 10)
#print(findNext(values))


