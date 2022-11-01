# https://www.hackerrank.com/challenges/merge-the-tools/problem

from textwrap import wrap
def merge_the_tools(string, k):
    for z in map(dict.fromkeys, wrap(string,k)):
        print("".join(z))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)