import copy

input = open("input.txt")

grid = []
for i in input:
    i = i.strip()
    grid.append([int(char) for char in i])

dist = []
for i in grid:
    dist.append([])
    for j in i:
        dist[-1].append(9999999999)
dist[0][0] = 0

# could be more efficient, but i wanted to code something myself and not just implement the algoritm
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
        dist = distance
        break
    dist = distance

print(dist[-1][-1])

# part 1: 613
