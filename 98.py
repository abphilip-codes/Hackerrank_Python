# https://www.hackerrank.com/challenges/validating-uid/problem

import re

pat = r"^(?=(?:[a-z\d]*[A-Z]){2})(?=(?:\D*\d){3})(?:([a-zA-Z\d])(?!.*\1)){10}$"
for _ in range(int(input())):
    if re.match(pat, input()):
        print("Valid")
    else:
        print("Invalid")