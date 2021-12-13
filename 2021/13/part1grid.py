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
            
for i in fold:
    if i[0] == "x":
        for j in range(len(grid)):
            new = ""
            for k in range(i[1] + 1, len(grid[j])):
                if grid[j][k] == "#":
                    new += "#"
                else:
                    new += grid[j][len(grid[j]) - k -1]
            grid[j] = new[::-1]
    else:
        for j in range(i[1], len(grid)):
            for k in range(len(grid[j])):
                if grid[j][k] == "#":
                    grid[len(grid) - j - 1] = grid[len(grid) - j - 1][:k] + "#" + grid[len(grid) - j - 1][k + 1:]
        for j in range(i[1], len(grid)):
            grid.pop(i[1])
    break

points = 0
for i in grid:
    print(i)
    for j in i:
        if j == "#":
            points += 1
print(points)

# part 1: 866 high, works for example, idk what im doing wrong
