# https://www.hackerrank.com/challenges/np-inner-and-outer/problem

import numpy as np
a = np.array(input().split(), int)
b = np.array(input().split(), int)
print(np.inner(a,b), np.outer(a,b), sep='\n')