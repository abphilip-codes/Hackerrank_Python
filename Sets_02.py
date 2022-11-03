# https://www.hackerrank.com/challenges/no-idea/problem

from collections import Counter

n, m = map(int, input().split())
c = Counter(list(map(int, input().split())))
a = set(map(int, input().split()))
b = set(map(int, input().split()))
k = 0

for z, f in c.items():
    if(z in a): k+=f
    if(z in b): k-=f
print(k)