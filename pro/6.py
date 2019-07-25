u=int(input())
v=list(map(int,input().split()))
w=0
for i in range(u):
    for j in range(i,u):
        for k in range(j,u):
            if(v[i]<v[j]<v[k]):
                w+=1
print(w)
