# Find the Runner-Up Score!

if __name__ == '__main__':
    a = int(input())
    l = list(map(int,input().strip().split()))[:a]
    b = max(l)
    while max(l) == b:
        l.remove(max(l))
    print (max(l))

