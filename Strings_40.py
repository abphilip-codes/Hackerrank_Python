# https://www.hackerrank.com/challenges/alphabet-rangoli/problem

def print_rangoli(n):
    from string import ascii_lowercase as chars
    h = [((
            '-'.join(chars[z:n])[::-1] + 
            '-'.join(chars[z:n])[1:]
        )).center(4*n-3, '-') for z in range(n)]
    print(*(h[::-1] + h[1:]), sep="\n")

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)