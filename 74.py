# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

n, a = int(input()), set(map(int,input().split()))
m, b = int(input()), set(map(int,input().split()))
print(len(a.symmetric_difference(b)))