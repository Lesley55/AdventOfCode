input = open("input.txt")
input = input.readlines()
input = [i.replace("\n", "") for i in input]

beams = [[0, -1, 0, 1]]
energized = []
loop = False
while 0 < len(beams) and not loop:
    loop = True
    new = []
    for b in range(len(beams)):
        pos = [beams[b][0] + beams[b][2], beams[b][1] + beams[b][3]]
        if 0 <= pos[0] and pos[0] < len(input) and 0 <= pos[1] and pos[1] < len(input[0]) and not pos + beams[b][2:] in energized:
            if input[pos[0]][pos[1]] == "|" and beams[b][3] != 0:
                new.append(pos + [1, 0])
                new.append(pos + [-1, 0])
            elif input[pos[0]][pos[1]] == "-" and beams[b][2] != 0:
                new.append(pos + [0, 1])
                new.append(pos + [0, -1])
            elif input[pos[0]][pos[1]] == "/":
                new.append(pos + [-beams[b][3], -beams[b][2]])
            elif input[pos[0]][pos[1]] == "\\":
                new.append(pos + [beams[b][3], beams[b][2]])
            else:
                new.append(pos + beams[b][2:])
            if not pos + beams[b][2:] in energized:
                energized.append(pos + beams[b][2:])
                loop = False
    beams = new
    new = []

distinct = []
for e in energized:
    if e[:2] not in distinct:
        distinct.append(e[:2])

print(len(distinct))

# part 1: 7236
