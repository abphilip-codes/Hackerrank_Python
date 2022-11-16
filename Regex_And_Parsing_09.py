# https://www.hackerrank.com/challenges/validating-named-email-addresses/problem

import re

exp = r"<[a-z][a-zA-Z0-9\-\.\_]+\@[a-zA-Z]+\.[a-zA-Z]{1,3}>"
for _ in range(int(input())):
    s = list(map(str, input().split()))
    if re.search(exp, s[1]): print(*s)