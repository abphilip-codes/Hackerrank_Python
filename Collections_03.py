# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

from collections import namedtuple

n, i = (int(input()), input().split())
info = namedtuple("info", i)
l = [int(info._make(input().split()).MARKS) for _ in range(n)]
print(sum(l)/len(l))