a = input()
target = ["a!", "b@"]

for item in target:
    while item in a:
        a = a.replace(item, '')

print(a)