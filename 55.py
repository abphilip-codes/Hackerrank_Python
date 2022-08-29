# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem

from collections import OrderedDict as od

n, o, a = int(input()), od(), []
for _ in range(n):
    k = input().split()
    a.append([" ".join(k[:len(k)-1]), int(k[len(k) - 1])])
    o.update({" ".join(k[:len(k)-1]): int(k[len(k) - 1])})

for z in a: o[z[0]] = a.count(z) * z[1]
for z in o.keys(): print(z, str(o[z]))