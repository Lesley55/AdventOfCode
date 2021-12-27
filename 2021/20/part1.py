inp = open("input.txt")

iea = ""
image = []
enhance = 2 # part 1
enhance = 50 # part 2

first = True
for i in inp:
    i = i.strip()
    if first:
        iea = i
        first = False
    elif i != "":
        image.append(i)

inputimg = {}
y, x = len(image), len(image[0])
for i in range(y):
    for j in range(x):
        if image[i][j] == "#":
            inputimg[(i,j)] = True

surrounding = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]
for e in range(enhance):
    outputimg = {}
    for i in range(-1 * enhance - enhance, y + enhance + enhance):
        for j in range(-1 * enhance - enhance, x + enhance + enhance):
            bit = ""
            for s in surrounding:
                if (i + s[0], j + s[1]) in inputimg:
                    bit += "1"
                else:
                    bit += "0"
            if iea[int(bit, 2)] == "#":
                outputimg[(i,j)] = True
    inputimg = outputimg

lit = 0
for i in range(-1 * enhance, y + enhance):
    for j in range(-1 * enhance, x + enhance):
        if (i,j) in inputimg:
            lit += 1
print(lit)

# part 1: 5268
# part 2: 16875