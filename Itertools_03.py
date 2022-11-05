# https://www.hackerrank.com/challenges/itertools-combinations/problem

from itertools import combinations
s, k = input().split()
for z in range(1, int(k)+1):
    for y in list(combinations(sorted(s), z)): print(''.join(y))