# https://www.hackerrank.com/challenges/incorrect-regex/problem

import re
for z in range(int(input())):
    try:
        reg = re.compile(input())
        print("True")
    except re.error: print("False")