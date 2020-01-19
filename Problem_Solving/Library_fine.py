a,b,c=input().split()
x,y,z=input().split()
fine=0
a=int(a)
b=int(b)
c=int(c)
x=int(x)
y=int(y)
z=int(z)
if(c>z):
    fine=fine+10000
elif(c>=z and b>y):
    fine=fine+500*(b-y)
elif(c==z and b>=y and a>x):
    fine=fine+15*(a-x)
print(fine)
