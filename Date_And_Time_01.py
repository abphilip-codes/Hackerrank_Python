# https://www.hackerrank.com/challenges/calendar-module/problem

import calendar as cal

l = list(map(int, reversed(str(input()).split())))
print(list(cal.day_name)[cal.weekday(l[0], l[2], l[1])].upper())