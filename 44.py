# https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter
num, sizes, ans = int(input()), Counter(map(int, input().split())), 0
for _ in range(int(input())):
    s, price = map(int, input().split())
    if(sizes[s]): ans, sizes[s] = ans+price, sizes[s]-1
print(ans)