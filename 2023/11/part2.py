input = open("input.txt")
input = input.readlines()

galaxies = []
for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == "#":
            galaxies.append([i, j])

empty = []
for i in range(len(input)):
    input[i] = input[i].replace("\n", "")
    if not "#" in input[i]:
        empty.append(i)
for i in empty[::-1]:
    for g in range(len(galaxies)):
        if i < galaxies[g][0]:
            galaxies[g][0] += 999999

empty = []
for j in range(len(input[0])):
    e = True
    for i in range(len(input)):
        if input[i][j] == "#":
            e = False
    if e:
        empty.append(j)
for j in empty[::-1]:
    for g in range(len(galaxies)):
        if j < galaxies[g][1]:
            galaxies[g][1] += 999999

total = 0
for g in range(len(galaxies)):
    for n in range(g + 1, len(galaxies)):
        total += abs(galaxies[g][0] - galaxies[n][0]) + abs(galaxies[g][1] - galaxies[n][1])

print(total)

# part 2: 543018317006
