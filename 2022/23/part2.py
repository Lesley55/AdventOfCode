input = open("input.txt")

scan = []
for i in input:
    i = i.strip()
    scan.append(i)

elves = set()
for y in range(len(scan)):
    for x in range(len(scan[0])):
        if scan[y][x] == "#":
            elves.add((y, x))

nswe = [[(-1, 0), (-1, -1), (-1, 1)], [(1, 0), (1, -1), (1, 1)], [(0, -1), (-1, -1), (1, -1)], [(0, 1), (-1, 1), (1, 1)]]
direction = 0
round = 0
while True:
    round += 1
    proposed = {}
    for elf in elves:
        # if no elf in surrounding, don't move
        surrounding = False
        for i in range(-1, 2):
            for j in range(-1, 2):
                if not (i == 0 and j == 0) and (elf[0] + i, elf[1] + j) in elves:
                    surrounding = True
                    break
        if not surrounding:
            continue
        # propose to move
        for i in range(direction, direction + len(nswe)):
            adjacent = False
            for j in nswe[i % len(nswe)]:
                if (elf[0] + j[0], elf[1] + j[1]) in elves:
                    adjacent = True
            if not adjacent:
                proposed[elf] = (elf[0] + nswe[i % len(nswe)][0][0], elf[1] + nswe[i % len(nswe)][0][1])
                break
    # remove double proposed
    new_proposed = {}
    for i in proposed:
        double = False
        for j in proposed:
            if i != j and proposed[i] == proposed[j]:
                double = True
                break
        if not double:
            new_proposed[i] = proposed[i]
    # move
    new_elves = set()
    for i in elves:
        if i in new_proposed:
            new_elves.add(new_proposed[i])
        else:
            new_elves.add(i)
    if elves == new_elves:
        break
    elves = new_elves
    # change propose direction order
    direction = (direction + 1) % len(nswe)

print(round)
# part 2: 935
