s=0
x=int(input())
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    s+=(a*b)
if s==x:
    print("Yes")
else :
    print("No")

