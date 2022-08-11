# https://www.hackerrank.com/challenges/python-string-formatting/problem

def print_formatted(n):
    w = len("{0:b}".format(n))
    for z in range(1, n+1):
        print("{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format(z, w=w))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)