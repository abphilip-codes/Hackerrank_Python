# https://www.hackerrank.com/challenges/python-time-delta/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def time_delta(t1, t2):
    from dateutil.parser import parse as p
    return str(abs(int((p(t1)-p(t2)).total_seconds())))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        fptr.write(delta + '\n')

    fptr.close()