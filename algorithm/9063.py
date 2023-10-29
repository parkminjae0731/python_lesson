z=int(input())
x=[0]*z
y=[0]*z
for i in range(z):
    a,b=map(int,input().split())
    x[i]=a
    y[i]=b
c=max(x)-min(x)
d=max(y)-min(y)
print(c*d)