a,b,c=map(int,input().split(' '))
d=0
e=0
while True:
    d+=a
    e+=a
    if d>=c:
        print(e/a)
        break
    else :
        d-b
        
   