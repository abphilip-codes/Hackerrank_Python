# https://www.hackerrank.com/challenges/python-mod-divmod/problem

x, y = int(input()), int(input())
print(x//y, x%y, divmod(x,y), sep='\n')