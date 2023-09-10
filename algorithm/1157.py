l = [0] * 26
s = input()
s = s.upper()

for i in range(len(s)):
    l[ord(s[i]) - ord("A")] += 1

if l.count(max(l))>=2:
    print("?")
elif l.count(max(l))==1:
    print(chr((l.index(max(l)))+ord("A")))