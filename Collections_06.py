# https://www.hackerrank.com/challenges/py-collections-deque/problem

from collections import deque
d = deque()
for _ in range(int(input())):
    c, *n = input().split()
    eval("d.{0}(*n)".format(c))
print(*d)