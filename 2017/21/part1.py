input = open("input.txt")
input = input.readlines()

rules = []
for i in input:
    r = []
    for j in i.strip().split(" => "):
        r.append(j.split("/"))
    rules.append(r)

grid = [".#.", "..#", "###"]

def flip(square):
    return [i[::-1] for i in square]

def rotate(square):
    square = flip(square)
    new = []
    for i in range(len(square)):
        new.append("")
        for j in range(len(square[i])):
            new[i] += square[j][i]
    return new

def check(square):
    for i in rules:
        if square == i[0]:
            return i[1]
    return False

def getReplacement(square):
    r = check(square)
    if r:
        return r
    for i in range(3):
        square = rotate(square)
        r = check(square)
        if r:
            return r
    square = flip(square)
    r = check(square)
    if r:
        return r
    for i in range(3):
        square = rotate(square)
        r = check(square)
        if r:
            return r

# for i in range(5): # part 1
for i in range(18): # part 2
    divsible = 2 if len(grid) % 2 == 0 else 3
    newgrid = ["" for s in range(int(len(grid) / divsible * (divsible + 1)))]
    for j in range(0, len(grid), divsible):
        for k in range(0, len(grid[j]), divsible):
            square = [grid[j + i][k: k + divsible] for i in range(divsible)]
            replacement = getReplacement(square)
            for l in range(len(replacement)):
                newgrid[int(j/divsible*(divsible+1))+l] += replacement[l]

    grid = newgrid

total = 0
for i in grid:
    total += i.count("#")

print(total)

# part 1: 110
# part 2: 1277716
