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

b = 0
for beacon in beacons:
    if beacon[1] == row:
        b += 1

no = set()
for i in sensors:
    dist = abs(i[2] - i[0]) + abs(i[3] - i[1])
    x = dist - (row - i[1])
    for j in range(-x, x + 1):
        d = abs(i[0] + j - i[0]) + abs(row - i[1])
        if d <= dist:
            no.add(i[0] + j)

print(len(no) - b)
# part 1: 5564017
