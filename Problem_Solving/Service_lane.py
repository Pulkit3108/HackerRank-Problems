a,b=map(int,input().split())
c=list(map(int,input().split()))
for p in range(0,b):
    i,j=map(int,input().split())
    x=c[i]
    for m in range(i,j+1):
        x=min(x,c[m])
    print(x)
