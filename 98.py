# https://www.hackerrank.com/challenges/validating-uid/problem

import re

exp = r"^(?=(?:[a-z\d]*[A-Z]){2})(?=(?:\D*\d){3})(?:([a-zA-Z\d])(?!.*\1)){10}$"
for _ in range(int(input())):
    print("Valid" if(re.match(exp, input())) else "Invalid")