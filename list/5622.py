base=["ABC", "DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ" ]
#a=str(input())
# WA => [9 2]
# UNUCIC => [8, 6, 8, 2, 4, 2]
# c=0
s=str(input())
a = []
for i in range(len(base)):
    for u in s:
        if u in base[i]:
            # c+=i+3
            a.append(i+3)
# print(c)
print((a))





