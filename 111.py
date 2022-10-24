# https://www.hackerrank.com/challenges/validating-credit-card-number/problem

import re
r = [str(z)*4 for z in range(10)]
for _ in range(int(input())):
    reg = re.match(r'(^[4|5|6]\d{3})+?-?(\d{4})+?-?(\d{4})+?-?(\d{4})$', input())
    k = reg.group().replace('-','') if(reg) else ''
    if(reg and all([k[z:z+4] not in r for z in range(len(k)-3)])): print('Valid')
    else: print('Invalid')