N,M=map(int,input().split())
data = list(map(int, input().split())) 
ans=0
for a in range(N-2):
    for b in range(a+1, N-1):
        for c in range(b+1, N):
            if data[a]+data[b]+data[c]<=M:
                ans = max(ans,data[a]+data[b]+data[c])
print(ans)
