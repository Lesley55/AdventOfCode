input = open("input.txt")

sensors = []
for i in input:
    i = i.strip()
    i = i.replace("=", " ").replace(",", " ").replace(":", " ")
    i = i.split()
    sensors.append([int(i[3]), int(i[5]), int(i[11]), int(i[13])])

boundary = 4000000
distances = []
for i in sensors:
    dist = abs(i[2] - i[0]) + abs(i[3] - i[1])
    distances.append(dist)

for i in range(len(sensors)):
    out = distances[i] + 1
    for x in range(out + 1):
        coords = (sensors[i][0] + x, sensors[i][1] + out - x)
        if 0 <= coords[0] and coords[0] <= boundary and 0 <= coords[1] and coords[1] <= boundary:
            possible = True
            if possible:
                for j in range(len(sensors)):
                    dist = abs(coords[0] - sensors[j][0]) + abs(coords[1] - sensors[j][1])
                    if dist <= distances[j]:
                        possible = False
                        break
            if possible:
                print(coords[0] * 4000000 + coords[1])

# part 2: 11558423398893
