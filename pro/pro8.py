def gcd(m1,m2):
    z=0
    m3=min(m1,m2)
    for k in range(m3,1,-1):
        if m1%k==0 and m2%k==0:
            return k
            z=1
    if z!=1:
        return 1

o=input()
b=o.split(" ")
c=[]
e=[]
res=[]
c1=int(b[0])
c2=int(b[1])
c3=input()
d=c3.split(" ")
for i in range(len(d)):
    e.append(int(d[i]))
for j in range(c2):
    f=input()
    g=f.split(" ")
    g1=int(g[0])-1
    g2=int(g[1])-1
    #print(g1,g2)
    #print(e[g1],e[g2])
    s=gcd(e[g1],e[g2])
    res.append(s)
for y in res:
    print(str(y))

    
  
