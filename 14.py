# https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem

for i in range(int(input())):
    line = input()
    
    while ' && ' in line or ' || ' in line:
        line = line.replace(" && ", " and ").replace(" || ", " or ")
    
    print(line)

