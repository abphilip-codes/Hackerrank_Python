# https://www.hackerrank.com/challenges/matrix-script/problem

#!/bin/python3

import math
import os
import random
import re
import sys


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

print (
    re.sub(r'\b([^a-zA-Z0-9]+?)\b', ' ',
    ''.join([matrix[z][y] for y in range(m) for z in range(n)]))
)