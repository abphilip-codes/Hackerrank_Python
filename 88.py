# https://www.hackerrank.com/challenges/re-start-re-end/problem

import re

s, k = input(), input()
indexes = [(m.start(), m.end() + (len(k) -1)) for m in re.finditer(rf"(?={k})", s)]

if len(indexes) > 0:
    for z in indexes: print(z)
else: print((-1, -1))