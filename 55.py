# https://www.hackerrank.com/challenges/symmetric-difference/problem

x, a = int(input()), set(map(int,input().split()))
y, b = int(input()), set(map(int,input().split()))
for z in sorted(a.symmetric_difference(b)): print(z)