n=int(input())
for i in range(0,n):
    a,b,c=input().split()
    a=int(a)
    b=int(b)
    c=int(c)
    if(a==1 and c==1):
        print(a)
    else:
        if(b<=(a-c+1)):
            print(c+b-1)
        else:
            x=b%a
            if(x==0 and c==1):
                print(a)
            elif((x+c-1)<=a):
                print(x+c-1)
            else:
                print(x-(a-c)-1)


