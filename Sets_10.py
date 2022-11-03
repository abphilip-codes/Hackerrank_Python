# https://www.hackerrank.com/challenges/py-set-mutations/problem

n, a = int(input()), set(map(int, input().split()))
for _ in range(int(input())):
    func, *t = input().split()
    k = set(map(int, input().split()))    
    eval(f'a.{func}({k})')
print(sum(a))