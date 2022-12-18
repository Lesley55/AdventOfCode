input = open("input.txt")

cubes = []
for i in input:
    i = i.strip()
    i = i.split(",")
    for j in range(len(i)):
        i[j] = int(i[j])
    cubes.append(tuple(i))

sides = [(0,0,1), (0,0,-1), (0,1,0), (0,-1,0), (1,0,0), (-1,0,0)]
surface = 0

next = [(-1,-1,-1)]
visited = set()
while len(next) > 0:
    current = next.pop(0)
    bound = True
    for i in current:
        if i < -1 or i > 22:
            bound = False
    if bound and not current in visited:
        visited.add(current)
        for s in sides:
            neighbor = (current[0] + s[0], current[1] + s[1], current[2] + s[2])
            if neighbor in cubes:
                surface += 1
            else:
                next.append(neighbor)

print(surface)
# part 2: 2582
