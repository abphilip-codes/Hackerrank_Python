# https://www.hackerrank.com/challenges/word-order/problem

from collections import OrderedDict
dict = OrderedDict()
s = int(input())
for i in range(0,s):
    a = input()
    if(a not in dict.keys()):
        dict.update({a:1})
        continue
    dict[a]+=1
print(len(dict.keys()))
print(*dict.values())

