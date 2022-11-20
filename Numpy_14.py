# https://www.hackerrank.com/challenges/np-polynomials/problem

import numpy
a = list(map(float,input().split()));
b = input();
s = numpy.polyval(a,int(b));
print(s)