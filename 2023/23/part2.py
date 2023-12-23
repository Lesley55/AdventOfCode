input = open("input.txt")
input = input.readlines()
for i in range(len(input)):
    input[i] = input[i].replace("\n", "")
input[0] = "##" + input[0][2:]

pos = [[1, 1, 1, [1,1], []]]
end = [len(input) - 1, len(input[-1]) - 2]
cross = []
while 0 < len(pos):
    p = pos.pop(-1)
    n = 0
    for i in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        if input[p[0] + i[0]][p[1] + i[1]] != "#":
            n += 1
    if 2 < n:
        cross.append([p[:2], p[2], p[3]])
    for i in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        new = [p[0] + i[0], p[1] + i[1]]
        if new == end:
            cross.append([end, p[2] + 1, p[3]])
            continue
        if input[new[0]][new[1]] != "#" and not new in p[4] and not [new, p[2] + 1, p[3]] in cross:
            prev_cross = p[3]
            if 2 < n:
                prev_cross = p[:2]
                pos.append([new[0], new[1], 1, prev_cross, [p[:2]]])
            else:
                pos.append([new[0], new[1], p[2] + 1, prev_cross, [p[:2]] + p[4]])

dist = []
for c in cross:
    if not c in dist and not c[::-1] in dist:
        dist.append(c)

pos = [[1, 1, 0, []]]
longest = 0
while 0 < len(pos):
    p = pos.pop(-1)
    if p[:2] == end:
        if longest < p[2]:
            longest = p[2]
            print(longest)
        continue
    for d in dist:
        if p[:2] == d[0] and not d[2] in p[3]:
            pos.append([d[2][0], d[2][1], p[2] + d[1], [p[:2]] + p[3]])
        elif p[:2] == d[2] and not d[0] in p[3]:
            pos.append([d[0][0], d[0][1], p[2] + d[1], [p[:2]] + p[3]])

print(longest)

# part 2: 6598
