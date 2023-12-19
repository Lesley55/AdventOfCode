input = open("input.txt")

pos = [0, 0]
directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
points = []

for i in input:
    i = i.split()
    d = int(i[2][7])
    distance = int(i[2][2:7], 16)
    pos = [pos[0] + (directions[d][0] * distance), pos[1] + (directions[d][1] * distance)]
    points.append(pos)

area = 0
# strip away squares from the side
while 2 < len(points):
    print(len(points))
    points.sort(key=lambda x: (x[1], x[0]))
    lu, ld = points.pop(0), points.pop(0)
    for p in range(len(points)):
        if lu[0] < points[p][0] and points[p][0] < ld[0] and not ld[0] == points[p + 1][0]:
            points += [lu, ld] # put back in
            # turn entire map to strip from next side
            points.sort(key=lambda x: x[0])
            maxy = points[-1][0]
            for p in range(len(points)):
                points[p] = [points[p][1], maxy - points[p][0]]
            break
        if lu[0] == points[p][0] or ld[0] == points[p][0]:
            area += (ld[0] - lu[0] + 1) * (points[p][1] - lu[1] + 1)
            mu, md = [lu[0], points[p][1]], [ld[0], points[p][1]]
            a, b = False, False
            if mu in points:
                points.pop(points.index(mu))
            else:
                points.append(mu)
                a = True
            if md in points:
                points.pop(points.index(md))
            else:
                points.append(md)
                b = True
            if 2 < len(points):
                if a != b:
                    for i in points:
                        if i[1] == mu[1] and mu[0] < i[0] and i[0] < md[0]:
                            if a:
                                md = i
                            elif b:
                                mu = i
                            break
                area -= md[0] - mu[0] + 1
            break

print(area)

# part 2: 
