# Check Strict Superset

a = set(map(str, input().split(' ')))
ss = []
for i in range(int(input())):
     ss.append(a.issuperset(set(map(str, input().split(' ')))))
print(all(ss))

