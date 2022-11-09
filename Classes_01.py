# https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem

import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        a, b, c, d = self.real, self.imaginary, no.real, no.imaginary
        return Complex(a+c, b+d)
        
    def __sub__(self, no):
        a, b, c, d = self.real, self.imaginary, no.real, no.imaginary
        return Complex(a-c, b-d)
    
    def __mul__(self, no):
        a, b, c, d = self.real, self.imaginary, no.real, no.imaginary
        r = a*c - b*d
        i = a*d + b*c
        return Complex(r, i)
    
    def __truediv__(self, no):
        a, b, c, d = self.real, self.imaginary, no.real, no.imaginary
        r = (a*c + b*d) / (c**2 + d**2)
        i = (b*c - a*d) / (c**2 + d**2)
        return Complex(r, i)

    def mod(self):
        return Complex(math.sqrt(self.real**2 + self.imaginary**2), 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')