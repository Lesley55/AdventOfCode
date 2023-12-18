input = open("input.txt")

pos = [0, 0]
holes = [[0, 0]]
directions = {"R": [0, 1], "L": [0, -1], "U": [-1, 0], "D": [1, 0]}

for i in input:
    i = i.split()
    for j in range(int(i[1])):
        pos = [pos[0] + directions[i[0]][0], pos[1] + directions[i[0]][1]]
        ## if already a hole at position it should dig the next, because every number should dig, and you cant dig already removed ground, but apperently it either wont cross, or the question didnt take this into account, but should have to be included in my opinion, the way it was written.
        # while pos in holes and not pos == [0, 0]:
        #     pos = [pos[0] + d[i[0]][0], pos[1] + d[i[0]][1]]
        if pos != [0, 0]:
            holes.append(pos)

holes.sort(key=lambda x: x[0])
miny, maxy = holes[0][0], holes[-1][0]
holes.sort(key=lambda x: x[1])
minx, maxx = holes[0][1], holes[-1][1]

inside = []
outside = []
for y in range(miny, maxy + 1):
    for x in range(minx, maxx + 1):
        adj = [[y, x]]
        more = False
        while True:
            more = False
            for k in adj:
                if not (k in outside or k in inside or k in holes):
                    for d in directions:
                        new = [k[0] + directions[d][0], k[1] + directions[d][1]]
                        if new[0] < miny or maxy < new[0] or new[1] < minx or maxx < new[1] or new in outside:
                            outside += adj
                            break
                        elif new in inside:
                            inside += adj
                            break
                        elif not new in holes and not new in adj:
                            adj.append(new)
                            more = True
                    else:
                        continue
                    break
                else:
                    break
            else:
                if not more:
                    inside += adj
                    break
                continue
            break

print(len(holes) + len(inside))

# part 1: 67891
