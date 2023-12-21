input = open("input.txt")
input = input.readlines()

pos = []
rocks = []
for i in range(len(input)):
    input[i] = input[i].replace("\n", "")
    for j in range(len(input[i])):
        if input[i][j] == "#":
            rocks.append([i, j])
        elif input[i][j] == "S":
            pos.append([i, j])

directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
steps = 0
while steps < 64:
    steps += 1
    new = []
    for p in pos:
        for d in directions:
            np = [p[0] + d[0], p[1] + d[1]]
            if 0 <= np[0] and np[0] < len(input) and 0 <= np[1] and np[1] < len(input[0]):
                if not np in rocks and not np in new:
                    new.append(np)
    pos = new

print(len(pos))

# part 1: 3697
