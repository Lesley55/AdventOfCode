input = open("input.txt")

map = []
path = ""
for i in input:
    map.append(i)
path = map[-1].strip()
path = path.replace("R", " R ").replace("L", " L ").split()
map = map[:-2]

board = set()
walls = set()
for y in range(len(map)):
    for x in range(len(map[y][:-1])):
        if map[y][x] != " ":
            board.add((y, x))
        if map[y][x] == "#":
            walls.add((y, x))

start = (0, 0)
while not start in board or start in walls:
    start = (0, start[1] + 1)

d = 0
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
current = start
for p in path:
    # move
    if p.isdigit():
        for i in range(int(p)):
            next = (current[0] + dir[d][0], current[1] + dir[d][1])
            # wrap around
            if not next in board:
                next = (current[0] - dir[d][0], current[1] - dir[d][1])
                while next in board:
                    next = (next[0] - dir[d][0], next[1] - dir[d][1])
                next = (next[0] + dir[d][0], next[1] + dir[d][1])
            # stop at wall
            if next in walls:
                break
            # move to next
            current = next
    # turn
    elif p == "R":
        d += 1
        if d > 3:
            d = 0
    elif p == "L":
        d -= 1
        if d < 0:
            d = 3

print(1000 * (current[0] + 1) + 4 * (current[1] + 1) + d)
# part 1: 29408
