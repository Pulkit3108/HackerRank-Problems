n=int(input())
for i in range(0,n):
    count=0
    arr=[]
    a=int(input())
    b=int(a)
    while(a!=0):
        c=int(a%10)
        arr.append(c)
        a=int(a/10)
    for j in range(0,len(arr)):
        if(arr[j]==0):
            continue
        else:
            if(b%arr[j]==0):
                count=count+1




    print(count)
