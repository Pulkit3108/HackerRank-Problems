n=int(input())
arr=list(map(int,input().split()))
for i in range(1,len(arr)):
    key=arr[i]
    j=i-1
    while(arr[j]>key and j>=0):
        arr[j+1]=arr[j]
        j=j-1
    arr[j+1]=key
    print(' '.join(str(j) for j in arr))
    
        
    
