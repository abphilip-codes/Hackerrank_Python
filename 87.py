# https://www.hackerrank.com/challenges/re-findall-re-finditer/problem

import re
a = re.findall(r"(?<=[^aeiouAEIOU])([aeiouAEIOU]{2,})(?=[^aeiouAEIOU])", input())
print(*a if(a) else -1, sep="\n")