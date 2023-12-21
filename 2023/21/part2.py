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

even = 1
# odd = 0
directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
steps = 0
prev = []
while steps < 5000:
    steps += 1
    new = []
    for p in pos:
        for d in directions:
            np = [p[0] + d[0], p[1] + d[1]]
            if not [np[0] % len(input), np[1] % len(input[0])] in rocks and not np in new and not np in prev:
                new.append(np)
                if steps % 2 == 0:
                    even += 1
                # else:
                #     odd += 1
    prev = pos
    pos = new

if steps % 2 == 0:
    print(even)
# else:
#     print(odd)

# part 2: 
