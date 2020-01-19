n=int(input())
a=list(map(int,input().split()))
for i in range(1,n+1):
    for j in range(0,len(a)):
        if(a[a[j]-1]==i):
            print(j+1)

   
 
