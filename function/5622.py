def p(s):
    base=["ABC", "DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ" ]
    c=0
    a=[0]*len(base)
    for i in range(len(base)):
        for u in s:
            if u in base[i]:
                c+=i+3
    print(c)
s=str(input())
p(s)

