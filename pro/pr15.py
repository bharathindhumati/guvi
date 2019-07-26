g=int(input())
s=list(map(int,input().split()))
m=[]
for i in range(g):
    s.sort(reverse=True)
print(*s,sep="\n")
