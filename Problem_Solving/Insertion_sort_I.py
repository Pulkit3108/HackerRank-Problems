n=int(input())
a=list(map(int,input().split()))
x=a[n-1]
b=sorted(a)
for i in range(len(a)-1,0,-1):
    if(a[i-1]>x):
        a[i]=a[i-1]
    else:
        a[i]=x
    print(' '.join(str(j) for j in a))
    if(b==a):
        break;
if(a[0]==a[1]):
    a[0]=x
    print(' '.join(str(j) for j in a))

