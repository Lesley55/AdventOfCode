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
                # hardcoded for my input, not a great solution
                side = (int(current[0] / 50), int(current[1] / 50))
                cy, cx = current[0] % 50, current[1] % 50
                if side == (0, 1):
                    if d == 2:
                        next = (149 - cy, 0)
                    elif d == 3:
                        next = (150 + cx, 0)
                elif side == (0, 2):
                    if d == 0:
                        next = (149 - cy, 99)
                    elif d == 1:
                        next = (50 + cx, 99)
                    elif d == 3:
                        next = (199, cx)
                elif side == (1, 1):
                    if d == 0:
                        next = (49, 100 + cy)
                    elif d == 2:
                        next = (100, cy)
                elif side == (2, 0):
                    if d == 2:
                        next = (49 - cy, 50)
                    elif d == 3:
                        next = (50 + cx, 50)
                elif side == (2, 1):
                    if d == 0:
                        next = (49 - cy, 149)
                    elif d == 1:
                        next = (150 + cx, 49)
                elif side == (3, 0):
                    if d == 0:
                        next = (149, 50 + cy)
                    elif d == 1:
                        next = (0, 100 + cx)
                    elif d == 2:
                        next = (0, 50 + cy)
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
# part 2: 145360 to high
