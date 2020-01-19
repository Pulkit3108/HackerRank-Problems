# Enter your code here. Read input from STDIN. Print output to STDOUT
def kangaroo(x1,v1,x2,v2):
    if (v2 < v1) and ((x2 - x1) % (v2 - v1)) == 0:
        print("YES")
    else:
        print("NO")

x1,v1,x2,v2=map(int,input().split())
kangaroo(x1,v1,x2,v2)
