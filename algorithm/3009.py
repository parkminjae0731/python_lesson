c=[0]*3
d=[0]*3
e=[0]*2
for i in range(3):
    a,b=map(int,input().split())
    c[i]=a
    d[i]=b
if c[0]==c[1]:
    e[0]=c[2]    
elif c[0]==c[2]:
    e[0]=c[1]
elif c[2]==c[1]:
    e[0]=c[0] 
if d[0]==d[1]:
    e[1]=d[2]    
elif d[0]==d[2]:
    e[1]=d[1]
elif d[2]==d[1]:
    e[1]=d[0]
print(e[0],e[1])
#print(e[0],e[1])