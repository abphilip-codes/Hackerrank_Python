# https://www.hackerrank.com/challenges/iterables-and-iterators/problem

from itertools import combinations 

_, s = int(input()), list(combinations(input().split(), int(input())))
print(len([z for z in s if("a" in z)])/len(s))