# https://www.hackerrank.com/challenges/ginorts/problem

def sort_key(c):
    return (c in ('0', '2', '4', '6', '8'), c.isdigit(), c.isupper(), c)
    
print(*sorted(input(), key=sort_key), sep='')