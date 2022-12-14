input = open("input.txt")

cave = {}
for i in input:
    i = i.strip()
    i = i.split(" -> ")
    for j in range(len(i) - 1):
        point1 = i[j].split(",")
        point1 = (int(point1[0]), int(point1[1]))
        point2 = i[j + 1].split(",")
        point2 = (int(point2[0]), int(point2[1]))
        if point1[0] > point2[0] or point1[1] > point2[1]:
            point1, point2 = point2, point1
        for k in range(point1[0], point2[0] + 1):
            for l in range(point1[1], point2[1] + 1):
                cave[(l, k)] = "#"

lowest = 0
for rock in cave:
    if rock[0] > lowest:
        lowest = rock[0]

amount = 0
while True:
    sand = (0, 500)
    if sand in cave:
        break
    while True:
        if not (sand[0] + 1, sand[1]) in cave and sand[0] < lowest + 1:
            sand = (sand[0] + 1, sand[1])
        elif not (sand[0] + 1, sand[1] - 1) in cave and sand[0] < lowest + 1:
            sand = (sand[0] + 1, sand[1] - 1)
        elif not (sand[0] + 1, sand[1] + 1) in cave and sand[0] < lowest + 1:
            sand = (sand[0] + 1, sand[1] + 1)
        else:
            amount += 1
            cave[sand] = "o"
            break

print(amount)
# part 2: 27194
