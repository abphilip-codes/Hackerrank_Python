# Write a function

def is_leap(year):
    leap = False
    leap = year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
    return leap


