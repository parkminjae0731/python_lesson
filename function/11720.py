def solve(a):
    s = 0
    for c in a:
        s += int(c)
    return s

input()
a = input()

print(solve(a))