# https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem

import numpy as np

r, _ = map(int, input().split())
ar = np.array([list(map(int, input().split())) for _ in range(r)])
print(ar.T)
print(ar.flatten())