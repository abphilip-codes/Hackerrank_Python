# https://www.hackerrank.com/challenges/py-the-captains-room/problem

from collections import Counter

_, c = input(), Counter(tuple(map(int, input().split())))
print(c.most_common()[-1][0])