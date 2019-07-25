uvw=int(input())
sums=0
for i in range(0,uvw):
    if(pow(2,i)>uvw):
        break
    sums=uvw-pow(2,i)
print(sums)
