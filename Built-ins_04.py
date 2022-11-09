# https://www.hackerrank.com/challenges/python-sort-sort/problem

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    k = int(input())
    
    for z in sorted(arr, key = lambda x:x[k]):
        print(*z, end=' \n')