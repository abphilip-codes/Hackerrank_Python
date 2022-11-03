# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):
    a = set(array)
    return ('%.3f' % (sum(a)/len(a)))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)