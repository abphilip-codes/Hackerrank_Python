# https://www.hackerrank.com/challenges/introduction-to-regex/problem

import re

n, r = int(input()), r"^[-+]?\d*[.]\d*$"
[print(bool(re.match(r, input()))) for _ in range(n)]