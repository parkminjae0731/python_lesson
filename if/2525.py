a,b=map(int,input().split())
c = int(input())

# 80 => 1시간 20분
# 200 => 3H 20M
# 140 => 2H 20M
b+=c
if b>=60:
    a+=(b//60)
    b%=60 # 120 + 20
if a>=24:
    a-=24
print(a, b)