input = open("input.txt")

df = {}

for i in input:
    j = i.strip().split()
    k = j[0].split("-")
    df[(int(k[1][1:]), int(k[2][1:]))] = [int(j[1][:-1]), int(j[2][:-1])] # (x, y) = [Size, Used]

# simplify: almost all size > 80, almost all used < 80, removing exceptions, all used > avail, so can only move to empty
simple = {}
for i in df:
    if not df[i][0] > 500:
        if df[i][1] == 0:
            simple[i] = True
        else:
            simple[i] = False

# shortest path from top right to top left
right = 0
for i in simple:
    x, y = i
    if x == 0 and y > right:
        right = y

possible = [[[], 0, right, 0, 0, (-1,-1)]]
previous = []

found = False
def path(par):
    global found
    if not found:
        path, posX, posY, desX, desY, skip = par
        if posX != desX or posY != desY:
            connections = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for i in connections:
                pos = (posX + i[0], posY + i[1])
                if pos != skip and pos in simple and pos != (posX, posY) and not pos in previous:
                    previous.append(pos)
                    path.append([posX + i[0], posY + i[1]])
                    possible.append([path, posX + i[0], posY + i[1], desX, desY, skip])
        else:
            found = True
            return path

i = 0
p = False
while not found and i < len(possible):
    p = path(possible[i])
    if p:
        print(p)
        break
    i += 1

# shortest path from last position to next in shortest path
steps = 0

# get empty one to start
for i in p:
    # shortest route from previous to next using path()
    pass

print(steps)

# ------------------------------------------------------------------------------------
# code is kinda bad, so taking the ez way out:
# empty starts at x 8, y 28
# blocking is one line at y 22 from x 2 till x end
# go around: 27 up + 8 left + 33 down to get to target position and
# then move every move up is 5 steps * 33 rows = 233 steps

# part 2: 233
