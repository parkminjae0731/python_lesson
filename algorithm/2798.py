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
            