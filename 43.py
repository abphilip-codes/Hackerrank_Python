# https://www.hackerrank.com/challenges/merge-the-tools/problem

from collections import OrderedDict
def merge_the_tools(string, k):
    for z in range(0,len(string),k):     
        print(''.join(list(OrderedDict.fromkeys(string[z:z+k]))))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)