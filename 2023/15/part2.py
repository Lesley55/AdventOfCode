input = open("input.txt")
input = input.readline().split(",")

boxes = [[] for i in range(256)]

def hash(i):
    h = 0
    for j in i:
        h += ord(j)
        h *= 17
        h %= 256
    return h

for i in input:
    if i[-1] == "-":
        h = hash(i[:-1])
        for b in range(len(boxes[h])):
            if boxes[h][b][0] == i[:-1]:
                boxes[h].pop(b)
                break
    else:
        h = hash(i[:-2])
        found = False
        for b in range(len(boxes[h])):
            if boxes[h][b][0] == i[:-2]:
                # boxes[h][b][1] == int(i[-1])
                # boxes[h][b] == [i[:-2], int(i[-1])]
                boxes[h][b].insert(1, int(i[-1]))
                found = True
                break
        if not found:
            boxes[h].append([i[:-2], int(i[-1])])

total = 0
for b in range(len(boxes)):
    for l in range(len(boxes[b])):
        total += (1 + b) * (1 + l) * boxes[b][l][1]

print(total)

# part 2: 247153
