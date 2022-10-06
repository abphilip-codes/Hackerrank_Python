# https://www.hackerrank.com/challenges/hex-color-code/problem

import re

exp, k = r"[\s:](#[0-9A-Fa-f]{3,6})", []
for _ in range(int(input())): k.extend(re.findall(exp, input()))
print(*k, sep='\n')