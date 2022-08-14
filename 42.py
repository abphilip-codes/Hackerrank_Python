# https://www.hackerrank.com/challenges/the-minion-game/problem

import math
import os
import random
import re
import sys

def solve(s):
    return " ".join([z.capitalize() for z in s.split(" ")])
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()