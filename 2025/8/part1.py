import math

input = open("input.txt")

boxes = []
circuits = []
for i in input:
    i = i.strip()
    i = i.split(",")
    i = [int(j) for j in i]
    boxes.append(i)
    circuits.append([i])

distances = []
for i in range(len(boxes)):
    for j in range(i+1, len(boxes)):
        d = math.sqrt((boxes[i][0] - boxes[j][0])**2 + (boxes[i][1] - boxes[j][1])**2 + (boxes[i][2] - boxes[j][2])**2)
        distances.append([d, boxes[i], boxes[j]])
        
distances.sort(key=lambda x: x[0])

for i in range(1000):
    pair = distances.pop(0)
    i1 = None
    i2 = None
    for c in range(len(circuits)):
        if pair[1] in circuits[c]:
            i1 = c
        if pair[2] in circuits[c]:
            i2 = c
    if i1 != i2:
        if i2 < i1:
            i1, i2 = i2, i1
        circuits[i1] += circuits.pop(i2)

circuits.sort(key=lambda x: len(x), reverse=True)

print(math.prod([len(x) for x in circuits[:3]]))

# part 1: 97384
