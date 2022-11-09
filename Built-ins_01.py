# https://www.hackerrank.com/challenges/zipped/problem

_, n = map(int, input().split())

a = [list(map(float, input().split())) for z in range(n)]
for z in list(zip(*a)): print(round(sum(z)/len(z),1)) 