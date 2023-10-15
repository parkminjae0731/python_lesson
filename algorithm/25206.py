c=20
e=0
a=[0]*20
for i in range(c):
    a[i]=input()
    if "A+" in a[i]:
        e+=4.5
    elif "A0" in a[i]:
        e+=4
    elif "B+" in a[i]:
        e+=3.5
    elif "B0" in a[i]:
        e+=3
    elif "C+" in a[i]:
        e+=2.5
    elif "C0" in a[i]:
        e+=2
    elif "D+" in a[i]:
        e+=1.5
    elif "D0" in a[i]:
        e+=1
    elif "P" in a[i]:
        c-=1

b=e/c
print(b)