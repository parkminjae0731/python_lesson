a,b,c=map(int,input().split())

#3개가 똑같다면 10000+같은수*1000
if a==b==c:
    print(10000+a*1000)
#2개가 같다면 1000+같은수*100
elif a==b:
    print(1000+a*100)
elif b==c:
    print(1000+b*100)
elif a==c:
    print(1000+a*100)
elif a>b and a>c:
    print(a*100)
elif b>a and b>c:
    print(b*100)
elif c>b and c>a:
    print(c*100)