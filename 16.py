# https://www.hackerrank.com/challenges/py-check-subset/problem

for i in range(int(input())):
    a = input()
    b = set(input().split())
    c = input()
    d = set(input().split())
    print(b.issubset(d))

