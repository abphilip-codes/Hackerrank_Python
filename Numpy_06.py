# https://www.hackerrank.com/challenges/np-eye-and-identity/problem

import numpy
print(str(numpy.eye(*map(int,input().split()))).replace('1',' 1').replace('0',' 0'))