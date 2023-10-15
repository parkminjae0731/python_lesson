a,b,c,d=map(int,input().split())
if a<=b and a<=c-a and a<=d-b:
    print(a)
elif b<=a and b<=c-a and b<=d-b:
    print(b)
elif c-a<=b and c-a<=a and c-a<=d-b:
    print(c-a)
else :
    print(d-b)