while True:
    a,b,c=map(int,input().split())
    if a==0 and b==0 and c==0:
        break
    elif a>=b+c or b>=a+c or c>=a+b:
        print("Invalid")
    elif a==b and a==c:
        print("Equilateral")
    elif a==b or a==c or b==c:
        print("Isosceles")
    elif a!=b and a!=c and b!=c:
        print("Scalene")
    