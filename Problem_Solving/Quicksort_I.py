n=int(input())
a=list(map(int,input().split()))
p=a[0]
f=[]
l=[]
for i in range(1,n):
    if(a[i]<p):
        f.append(a[i])
    if(a[i]>p):
        l.append(a[i])
f.append(p)
c=f+l
print(' '.join(str(j) for j in c))
