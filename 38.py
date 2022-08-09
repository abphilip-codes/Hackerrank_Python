# https://www.hackerrank.com/challenges/designer-door-mat/problem

x, y = map(int,input().split())
k = [('.|.'*(2*z + 1)).center(y, '-') for z in range(x//2)]
print('\x'.join(k + ['WELCOME'.center(y, '-')] + k[::-1]))