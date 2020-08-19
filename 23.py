# Dot and Cross

import numpy
a=int(input())
a1=numpy.array([list(map(int,input().split())) for _ in range(a)])
a2=numpy.array([list(map(int,input().split())) for _ in range(a)])
print(numpy.dot(a1,a2))

