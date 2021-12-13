input = open("input.txt")

inp = []
fold = []
for i in input:
    if i != "\n" and i[0] != "f":
        i = i.strip().split(",")
        inp.append([int(i[0]), int(i[1])])
    elif i[0] == "f":
        i = i.strip().split()
        a, b = i[2].split("=")
        fold.append([a, int(b)])
            
for i in fold:
    if i[0] == "x":
        for j in range(len(inp)):
            if inp[j][0] > i[1]:
                inp[j][0] = i[1] - (inp[j][0] - i[1])
    else:
        for j in range(len(inp)):
            if inp[j][1] > i[1]:
                inp[j][1] = i[1] - (inp[j][1] - i[1])
    # break # uncomment for part 1

x = max(i[0] for i in inp)
y = max(i[1] for i in inp)
grid = []
for i in range(y + 1):
    grid.append("")
    for j in range(x + 1):
        if [j, i] in inp:
            grid[-1] += "#"
        else:
            grid[-1] += "."

points = 0
for i in grid:
    print(i)
    for j in i:
        if j == "#":
            points += 1
print(points)

# part 1: 731
# part 2: zkaucfuc
