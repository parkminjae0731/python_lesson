a,b=map(int,input().split())
origin = []
sample1 = ["WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW"]
sample2 = ["BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB"]
for i in range(a):
    origin.append(input())

for i in range(a-8):
    for j in range(b-8):
        for r in range(i, i+8):
            for c in range(j, j+8):
                print(sample1[r]) #(origin[r][c])
            
        
