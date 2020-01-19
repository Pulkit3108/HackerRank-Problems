n=int(input())
a=list(map(int,input().split()))
for i in range(0,len(a)):
    min=i
    for j in range(i+1,len(a)):
        if(a[j]<a[min]):
            min=j
    t=a[i]
    a[i]=a[min]
    a[min]=t
    
print(' '.join(str(j) for j in a))
