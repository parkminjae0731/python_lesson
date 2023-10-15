e=[0]*20
a=[0]*20
c=20
g=0
for i in range(20):
    a[i]=input()
    if "A+" in a[i]:
        e[i]+=4.5
    elif "A0" in a[i]:
        e[i]+=4
    elif "B+" in a[i]:
        e[i]+=3.5
    elif "B0" in a[i]:
        e[i]+=3
    elif "C+" in a[i]:
        e[i]+=2.5
    elif "C0" in a[i]:
        e[i]+=2
    elif "D+" in a[i]:
        e[i]+=1.5
    elif "D0" in a[i]:
        e[i]+=1
    elif "P" in a[i]:
        c-=1
for i in range(20):
    if "4.0" in a[i]:
        e[i]*=4
    elif "3.0" in a[i]:
        e[i]*=3
    elif "2.0" in a[i]:
        e[i]*=2
    elif "1.0" in a[i]:
        e[i]*=1
for i in range(c):
    if "4.0" in a[i]:
        g+=4
    elif "3.0" in a[i]:
        g+=3
    elif "2.0" in a[i]:
        g+=2
    elif "1.0" in a[i]:
        g+=1


b=sum(e)/g
print(round(b,6))

