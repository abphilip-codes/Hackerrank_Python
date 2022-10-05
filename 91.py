# https://www.hackerrank.com/challenges/validating-the-phone-number/problem

import re

exp = r"^[789][0-9]{9}$"
for _ in range(int(input())):
    print('YES' if(re.search(exp, input())) else 'NO')