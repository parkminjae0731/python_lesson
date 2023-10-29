a,b=map(int,input().split())
sample1 = ["WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW"]
sample2 = ["BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB"]
d=0

for i in range(a):
    c=input()
    while True:
        if "WB" in c:
            d+=c.count("WB")
            c.replace("WB","")
        else :
            break
        
        
    while True:
        if "BW" in c:
            d+=c.count("BW")
            c.replace("BW","")
        else :
            break
        
        
print(d)
