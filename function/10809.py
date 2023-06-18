def q(s):
    alp = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(alp)):
        if alp[i] in s:
            print(s.index(alp[i]),end=' ')
        else :
            print(-1,end=' ')
s = input()
q(s)






