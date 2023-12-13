input = open("input.txt")
input = input.readlines()

empty = []
for i in range(len(input)):
    input[i] = input[i].replace("\n", "")
    if not "#" in input[i]:
        empty.append(i)
for i in empty[::-1]:
    input.insert(i, input[i])

empty = []
for j in range(len(input[0])):
    e = True
    for i in range(len(input)):
        if input[i][j] == "#":
            e = False
    if e:
        empty.append(j)
for j in empty[::-1]:
    for i in range(len(input)):
        input[i] = input[i][:j] + "." + input[i][j:]

galaxies = []
for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == "#":
            galaxies.append([i, j])

total = 0
for g in range(len(galaxies)):
    for n in range(g + 1, len(galaxies)):
        total += abs(galaxies[g][0] - galaxies[n][0]) + abs(galaxies[g][1] - galaxies[n][1])

print(total)

# part 1: 9403026
