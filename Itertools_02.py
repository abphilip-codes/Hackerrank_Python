# https://www.hackerrank.com/challenges/itertools-permutations/problem

from itertools import permutations
x, y = input("").split()
p = list(permutations(x,int(y)))
print(*sorted(list("".join(z) for z in p)), sep='\n')