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

# code is kinda bad, so taking the ez way out:
# first and second row don't have high blocking the way, so once in place its just 5 or 6 steps per side move for the target
# empty starts at x 8, y 28, road up is free, then around target, so just count the steps till x 0, y 27 
# = 9 steps to get in place
# then 27 times 5 steps = 135
# total 144 steps?

# doing this completely wrong, target = x 34 y 0 not x 0 y 28

# so again
# blocking at y 22 form x high to x 2
# around 28 left + (34 - 8 = 26 down) + 5 * 33
# = 219 steps

# part 2: 219 low ?
