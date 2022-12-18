input = open("input.txt")

cubes = []
for i in input:
    i = i.strip()
    i = i.split(",")
    for j in range(len(i)):
        i[j] = int(i[j])
    cubes.append(i)

surface = 0
sides = [[0,0,1], [0,0,-1], [0,1,0], [0,-1,0], [1,0,0], [-1,0,0]]
for i in cubes:
    for j in sides:
        neighbor = [i[0] + j[0], i[1] + j[1], i[2] + j[2]]
        if not neighbor in cubes:
            surface += 1

print(surface)
# part 1: 4628
