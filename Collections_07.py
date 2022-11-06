# https://www.hackerrank.com/challenges/most-commons/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter as c

if __name__ == '__main__':
    for z in c(sorted(input())).most_common(3):
        print(z[0],z[1])