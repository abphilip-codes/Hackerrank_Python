# https://www.hackerrank.com/challenges/py-set-add/problem

n, t = int(input()), set()
for _ in range(n): t.add(input())
print(len(t))