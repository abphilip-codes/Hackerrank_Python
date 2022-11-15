# https://www.hackerrank.com/challenges/re-start-re-end/problem

import re
s, k = input(), input()
x = [(m.start(), m.end() + (len(k) -1)) for m in re.finditer(rf"(?={k})", s)]

if(not x): print((-1, -1))
else: 
    for z in x: print(z)