a = input()
target = ["c=", "c-","dz=","d-","lj","nj","s=","z="]

for item in target:
    while item in a:
        a = a.replace(item, '_')

print(len(a))