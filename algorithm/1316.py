cnt = 0
for _ in range(int(input())):
    alp = [0] * 26
    line = input()
    flag = True

    for i in range(len(line)):
        at = ord(line[i]) - ord("a")
        
        if alp[at] == 1 and line[i]!=line[i-1]:
            flag = False
            break
        
        alp[at] = 1
    
    if flag == True:
        cnt += 1

print(cnt)