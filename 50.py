# https://www.hackerrank.com/challenges/exceptions/problem

for _ in range(1, int(input())+1):
    l = input().split()
    try: print(int(l[0])//int(l[1]))
    except ValueError as e: print('Error Code:', e)
    except ZeroDivisionError as e: print('Error Code:', e)