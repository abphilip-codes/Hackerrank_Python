# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

n, s = int(input()), set(map(int, input().split()))
for _ in range(int(input())):
    z, *k = input().split()
    if(z=="pop"): s.pop()
    if(z=="remove"): s.remove(int(k[0]))
    if(z=="discard"): s.discard(int(k[0]))
print(sum(s))