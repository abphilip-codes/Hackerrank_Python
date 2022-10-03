# https://www.hackerrank.com/challenges/map-and-lambda-expression/problem

cube = lambda x: x**3

def fibonacci(n):
    f0, f1 = 0, 1
    fib = []
    for _ in range(n):
        fib.append(f0)
        f0, f1 = f1, f0+f1
    return fib

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))