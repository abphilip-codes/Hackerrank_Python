# Polynomials

import numpy
a = list(map(float,input().split()));
b = input();
s = numpy.polyval(a,int(b));
print(s)

