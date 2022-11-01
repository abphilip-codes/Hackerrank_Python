# https://www.hackerrank.com/challenges/string-validators/problem

if __name__ == '__main__':
    s = input()
    for z in ['isalnum', 'isalpha', 'isdigit', 'islower', 'isupper']:
        print(any(eval("ch." + z + "()") for ch in s)) 