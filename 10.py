# Nested Lists

if __name__ == '__main__':
    d={} 
    for _ in range(int(input())): 
        n=input() 
        g=float(input()) 
        d[n]=g 
    v=d.values()
    s=sorted(list(set(v)))[1] 
    sl=[] 
    for key,value in d.items():  
        if value==s: 
            sl.append(key) 
    sl.sort() 
    for a in sl: 
        print(a)

