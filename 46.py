# https://www.hackerrank.com/challenges/polar-coordinates/problem

import cmath
z = complex(input())
print(abs(z), cmath.phase(z), sep= '\n')