n=int(input())
for i in range(n):
    a, b = map(str, input().split())
    
    for i in range(len(b)):
        print(b[i] * int(a), end='')
    
    print()