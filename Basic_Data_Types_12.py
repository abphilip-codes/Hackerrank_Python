# https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N, l = int(input()), []
    for _ in range(N):
        a = input().strip()
        if(a=="print"):
            print(l)
            continue
        p = a.split()
        getattr(l, p[0])(*(map(int, p[1:])))