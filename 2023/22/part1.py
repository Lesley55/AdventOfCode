input = open("input.txt")

bricks = []
for i in input:
    i = i.replace("~", ",").split(",")
    bricks.append([int(j) for j in i] + [[]])

bricks.sort(key=lambda x: min(x[2], x[5]))

# drop bricks
for b in range(len(bricks)):
    while True:
        if 1 < min(bricks[b][2], bricks[b][5]):
            blocking = False
            for other in bricks:
                if max(other[2], other[5]) == min(bricks[b][2], bricks[b][5]) - 1:
                    if (bricks[b][0] <= other[0] and other[0] <= bricks[b][3]) or (bricks[b][0] <= other[3] and other[3] <= bricks[b][3]) or (other[0] < bricks[b][0] and bricks[b][3] < other[3]):
                        if (bricks[b][1] <= other[1] and other[1] <= bricks[b][4]) or (bricks[b][1] <= other[4] and other[4] <= bricks[b][4]) or (other[1] < bricks[b][1] and bricks[b][4] < other[4]):
                            blocking = True
                            bricks[b][-1].append(bricks.index(other)) # keep track of supporting bricks
            if not blocking:
                bricks[b] = [bricks[b][0], bricks[b][1], bricks[b][2] - 1, bricks[b][3], bricks[b][4], bricks[b][5] - 1, bricks[b][6]]
                continue
        break

total = 0
for b in range(len(bricks)):
    can = True
    for c in range(b + 1, len(bricks)):
        if b in bricks[c][6] and len(bricks[c][6]) < 2:
            can = False
    if can:
        total += 1

print(total)

# part 1: 454
