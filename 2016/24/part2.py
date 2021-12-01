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
count = 0
for i in map:
    for j in i:
        if j != "#" and j != ".":
            count += 1

next = [[{}, [["0"]], start[0], start[0], 0]]
found = []
moves = [[0,1], [0,-1], [1,0], [-1,0]]
def check(previous, shortest, x, y, steps):
    global found
    pos = map[x][y]
    if pos == "#" or (x,y) in previous or shortest in found:
        return
    a = False
    for i in shortest:
        if pos == i[0]:
            a = True
    if pos != "." and not a:
        shortest.append([pos, x, y, steps])
        previous = {}
    previous[(x,y)] = True
    if len(shortest) == count:
        found.append(shortest)
    for i in moves:
        next.append([previous, copy.copy(shortest), x + i[0], y + i[1], steps + 1])

def go():
    i = 0
    while i < len(next):
        check(next[i][0], next[i][1], next[i][2], next[i][3], next[i][4])
        i += 1

fewest = 9999999999
f = None
def few():
    global f, fewest
    for i in found:
        if i[-1][3] < fewest:
            fewest = i[-1][3]
            f = i

# part 1
go()
few()
print(fewest)

# part 2
next = [[{}, f[1:]] + f[-1][1:]]
print(next)
found = []
fewest = 9999999999
f = None
go()
few()
print(fewest)

# part 1: 490
# part 2: 
