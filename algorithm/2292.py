#1 6 12 18 24 30 36

#1 7 19 37 61 91 127
a=int(input())
b=1
c=1
while True:
    c+=(6*b)
    if a==1:
        print("1")
        break
    elif a in range(1,c+1):
        print(b+1)
        break
    
    b+=1
