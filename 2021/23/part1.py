import copy

inp = open("input.txt")

burrow = []
for i in inp:
    i = i.strip("\n").replace(" ", "#")
    burrow.append(i)

loc = {}
for y in range(len(burrow)):
    print(burrow[y])
    for x in range(len(burrow[y])):
        if burrow[y][x] != "#":
            loc[(y,x)] = burrow[y][x]
print(loc)

roomsX = [3,5,7,9]

possible = {loc: 0}
for p in possible:
    for i in possible[p]:
        if i != ".":
            # add possible steps
            loc = copy.copy(p)
            pass

# part 1: 
