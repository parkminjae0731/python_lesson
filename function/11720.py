def s(a,b):  
    ad=b%10
    b//10
    return ad
a=int(input())
b=int(input())
v=0
for i in range(a):
    v+=(s(a,b))
print(v)
