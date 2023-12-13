input = open("input.txt")

arrangements = 0

def check(s, g):
    global arrangements
    a = []
    for i in range(len(s)):
        if s[i] == "#":
            if i > 0 and s[i-1] == "#":
                a[-1] += 1
            else:
                a.append(1)
        elif s[i] == "?":
            check(s[:i] + "#" + s[i+1:], g)
            check(s[:i] + "." + s[i+1:], g)
            return
    if a == g:
        arrangements += 1

for i in input:
    i = i.split()
    springs = ""
    groups = []
    for j in range(5):
        springs += i[0] + "?"
        groups += [int(i) for i in i[1].split(",")]
    check(springs[:-1], groups)

print(arrangements)

# part 2: 
