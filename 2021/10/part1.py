input = open("input.txt")

corrupted = []
open = "{[(<"
chunks = {
    "}": "{",
    "]": "[",
    ")": "(",
    ">": "<",
}
for i in input:
    i = i.strip()
    current = []
    for j in i:
        if j in open:
            current.append(j)
        elif chunks[j] == current[-1]:
            current.pop(-1)
        else:
            corrupted.append(j)
            break

total = 0
for i in corrupted:
    if i == ")":
        total += 3
    elif i == "]":
        total += 57
    elif i == "}":
        total += 1197
    elif i == ">":
        total += 25137

print(total)

# part 1: 442131
