a,b,c=map(int,input().split(' '))
if (c-b)%(a-b)==0:
    print((c-b)//(a-b))
else:
    print((c-b)//(a-b)+1)

#d=0
#e=0
#while True:
    #d+=a
    #e+=a
    #if d>=c:
        #print(e//a)
        #break
    #d-=b