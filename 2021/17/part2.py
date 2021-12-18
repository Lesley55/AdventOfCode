target = [[117, 164], [-140, -89]]

minx = min(target[0])
maxx = max(target[0])
miny = min(target[1])
maxy = max(target[1])

hit = {}
def shoot(x, y):
    ix, iy = x, y
    velx, vely = x, y
    while x <= maxx and y >= miny:
        if minx <= x and maxy >= y:
            hit[(ix, iy)] = True
            return
        else:
            vely -= 1
            if velx < 0:
                velx += 1
            elif velx > 0:
                velx -= 1
            x += velx
            y += vely

for y in range(miny, abs(miny)):
    for x in range(maxx + 1):
        shoot(x, y)

print(len(hit))

# part 2: 4110
