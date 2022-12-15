input = open("input.txt")

sensors = []
beacons = {}
for i in input:
    i = i.strip()
    i = i.replace("=", " ").replace(",", " ").replace(":", " ")
    i = i.split()
    sensors.append([int(i[3]), int(i[5]), int(i[11]), int(i[13])])
    beacons[(int(i[11]), int(i[13]))] = True

row = 2000000

no = set()
for i in sensors:
    dist = abs(i[2] - i[0]) + abs(i[3] - i[1])
    for x in range(dist):
        for y in range(dist - x + 1):
            if i[1] + y == row and not (i[0] + x, i[1] + y) in beacons:
                no.add(i[0] + x)
            if i[1] - y == row and not (i[0] + x, i[1] - y) in beacons:
                no.add(i[0] + x)
            if i[1] + y == row and not (i[0] - x, i[1] + y) in beacons:
                no.add(i[0] - x)
            if i[1] - y == row and not (i[0] - x, i[1] - y) in beacons:
                no.add(i[0] - x)

print(len(no))
# part 1: 
