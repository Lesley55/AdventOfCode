input = open("input.txt")

patterns = [[]]
for i in input:
    if i == "\n":
        patterns.append([])
    else:
        patterns[-1].append(i.replace("\n", ""))

total = 0

def find_mirror(patterns, multiple):
    global total
    for p in patterns:
        for i in range(len(p) - 1):
            smudge = 0
            for j in range(min(i + 1, len(p) - i - 1)):
                for k in range(len(p[i - j])):
                    if p[i - j][k] != p[i + j + 1][k]:
                        smudge += 1
            if smudge == 1:
                total += (i + 1) * multiple
                break

find_mirror(patterns, 100)
flipped = []
for p in patterns:
    collumn = []
    for j in range(len(p[0])):
        row = ""
        for i in range(len(p)):
            row += p[i][j]
        collumn.append(row)
    flipped.append(collumn)
find_mirror(flipped, 1)

print(total)

# part 2: 35915
