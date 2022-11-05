# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem

from itertools import combinations_with_replacement as cwr
s, n = map(str, input().split())
for z in cwr(sorted(s), int(n)): print(''.join(z))