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
            if p[i] == p[i + 1]:
                mirror = True
                for j in range(min(i + 1, len(p) - i - 1)):
                    if p[i - j] != p[i + j + 1]:
                        mirror = False
                        break
                if mirror:
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

# part 1: 36041
