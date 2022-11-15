# https://www.hackerrank.com/challenges/re-group-groups/problem

import re 
a = re.findall(r"([A-Za-z0-9])\1+", input()) 
print(a[0] if(a) else -1)