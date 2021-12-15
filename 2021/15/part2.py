import copy

input = open("input.txt")

grid = []
for i in input:
    i = i.strip()
    grid.append([int(char) for char in i])

l = len(grid[0])
for i in range(4):
    for y in range(len(grid)):
        lg = len(grid[y])
        for x in range(lg - l, lg):
            if grid[y][x] + 1 <= 9:
                grid[y].append(grid[y][x] + 1)
            else:
                grid[y].append(1)

lg = len(grid)
for i in range(4):
    for y in range(len(grid) - lg, len(grid)):
        c = copy.deepcopy(grid[y])
        for x in range(len(c)):
            if c[x] + 1 <= 9:
                c[x] = c[x] + 1
            else:
                c[x] = 1
        grid.append(c)
    
dist = []
for i in grid:
    dist.append([])
    for j in i:
        dist[-1].append(9999999999)
dist[0][0] = 0

while True:
    distance = copy.deepcopy(dist)
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            possible = [[x + 1, y], [x - 1, y], [x, y - 1], [x, y + 1]]
            for i in possible:
                if 0 <= i[1] and i[1] < len(grid) and 0 <= i[0] and i[0] < len(grid[i[1]]):
                    d = distance[y][x] + grid[i[1]][i[0]]
                    if d < distance[i[1]][i[0]]:
                        distance[i[1]][i[0]] = d
    if dist == distance:
        break
    dist = distance

print(dist[-1][-1])

# part 2: 2899
