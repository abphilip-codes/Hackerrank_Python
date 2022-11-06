# https://www.hackerrank.com/challenges/piling-up/problem

for _ in range(int(input())):
    n, l = int(input()), list(map(int,input().split()))
    for z in range(n//2):
        if(l[z]<l[z+1] and l[n-z-1]<l[n-z-2]):
            print('No')
            break
    else: print('Yes')