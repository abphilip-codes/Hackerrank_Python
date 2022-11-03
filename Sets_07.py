# https://www.hackerrank.com/challenges/py-set-intersection-operation/problem

n, a = int(input()), set(map(int,input().split()))
m, b = int(input()), set(map(int,input().split()))
print(len(a.intersection(b)))