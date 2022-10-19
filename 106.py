# https://www.hackerrank.com/challenges/np-concatenate/problem

import numpy as np

n, m, _ = map(int, input().split())
a = [np.array(list(map(int, input().split()))) for _ in range(n+m)]
print(np.array(a))