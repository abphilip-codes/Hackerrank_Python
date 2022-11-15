# https://www.hackerrank.com/challenges/re-findall-re-finditer/problem

import re
a = re.findall(r"(?<=[^aeiouAEIOU])([aeiouAEIOU]{2,})(?=[^aeiouAEIOU])", input())
print(-1) if(not a) else print(*a, sep="\n")