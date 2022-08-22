# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

n, m = map(int, input().split())
d = {}
for z in range(n):
    x = input()
    d.setdefault(x, [])
    d[x].append(z+1)

for z in range(m):
    x = input()
    print(*d[x]) if(x in d) else print(-1)