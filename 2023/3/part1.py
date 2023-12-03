input = open("input.txt")

total = 0
engine = []

for i in input:
    engine.append(i.replace("\n", ""))

for i in range(len(engine)):
    number = ""
    part = False
    for j in range(len(engine[i])):
        if engine[i][j].isdigit():
            number += engine[i][j]
            for k in [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]:
                if 0 <= i+k[0] and i+k[0] < len(engine) and 0 <= j+k[1] and j+k[1] < len(engine[i+k[0]]):
                    if not engine[i+k[0]][j+k[1]].isdigit() and engine[i+k[0]][j+k[1]] != ".":
                        part = True
                        break
            if j+1 == len(engine[i]) or (j+1 < len(engine[i]) and not engine[i][j+1].isdigit()):
                if part:
                    total += int(number)
                number = ""
                part = False

print(total)

# part 1: 599832 high 529618
