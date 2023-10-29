<<<<<<< HEAD
N,M=map(int,input().split())
data = list(map(int, input().split())) 
ans=0
for a in range(N-2):
    for b in range(a+1, N-1):
        for c in range(b+1, N):
            if data[a]+data[b]+data[c]<=M:
                ans = max(ans,data[a]+data[b]+data[c])
print(ans)
=======
a,b=map(int,input().split())
data = list(map(int, input().split())) 
c=0
for a in range(len(data)-2):
    for b in range(1, len(data)-1):
        for c in range(2, len(data)):
            if data[a]+data[b]+data[c]>b:
                continue
            else:
                c=max(c,data[a]+data[b]+data[c])
print(c)
            
>>>>>>> 92f83844b46bddee820b2df57e63f68ade59c7ea
