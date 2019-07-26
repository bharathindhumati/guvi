u,v=map(int,input().split())
n=list(map(int,input().split()))
m=[]
for u in range(v):
       j,k=map(int,input().split())
       g=min(n[j-1:k])
       m.append(g)
for j in m:
       print(j)
