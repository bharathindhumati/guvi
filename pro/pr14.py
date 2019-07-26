u,v=map(int,input().split())
n=list(map(int,input().split()))
m=[]
for u in range(v):
       j=list(map(int,input().split()))
       m.append(j)
for i in m:
    a=0
    for k in range(i[0]-1,i[1]):
        a=a^n[k]
    print(a)    
