# https://www.hackerrank.com/challenges/swap-case/problem

def swap_case(s):
    return ''.join([z.lower() if(z.isupper()) else z.upper() for z in s])

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)