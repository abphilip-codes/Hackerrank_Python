# https://www.hackerrank.com/challenges/any-or-all/problem

_, l = int(input()), list(map(int, input().split()))
print(all([z>0 for z in l]) and any([str(z) == str(z)[::-1] for z in l]))