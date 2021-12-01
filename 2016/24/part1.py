import copy

input = open("input.txt")

# create map
map = []
for i in input:
    map.append(i.strip())

# get start position of 0
start = []
for i in range(len(map)):
    if "0" in map[i]:
        start = [i, map[i].index("0")]

# count numbers to go through
count = -1
for i in map:
    for j in i:
        if j != "#" and j != ".":
            count += 1

next = [[{}, [], start[0], start[0], 0]]
found = False
moves = [[0,1], [0,-1], [1,0], [-1,0]]
def check(previous, shortest, x, y, steps):
    global found
    pos = map[x][y]
    if pos == "#" or (x,y) in previous or found != False:
        return
    a = False
    for i in shortest:
        if pos == i[0]:
            a = True
    if pos != "." and pos != "0" and not a:
        shortest.append([pos, x, y, steps])
        previous = {}
    previous[(x,y)] = True
    if len(shortest) == count:
        found = shortest
    for i in moves:
        next.append([previous, copy.copy(shortest), x + i[0], y + i[1], steps + 1])

i = 0
while i < len(next):
    check(next[i][0], next[i][1], next[i][2], next[i][3], next[i][4])
    i += 1

print(found[-1][3])

# part 1: 490
