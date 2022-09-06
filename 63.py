# https://www.hackerrank.com/challenges/compress-the-string/problem

from itertools import groupby
for z in [list(g) for _, g in groupby(input())]:
    print("({}, {})".format(len(z), z[0]), end = ' ')