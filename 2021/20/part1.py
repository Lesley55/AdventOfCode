inp = open("input.txt")

iea = ""
image = []
enhance = 2

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
for e in range(1, enhance + 1):
    outputimg = {}
    for i in range(-1 * e, y + e):
        for j in range(-1 * e, x + e):
            bit = ""
            for s in surrounding:
                if (i + s[0], j + s[1]) in inputimg:
                    bit += "1"
                else:
                    bit += "0"
            if iea[int(bit, 2)] == "#":
                outputimg[(i,j)] = True
    inputimg = outputimg

    for i in range(-1 * e, y + e):
        p = ""
        for j in range(-1 * e, x + e):
            if (i,j) in outputimg:
                p += "#"
            else:
                p += "."
        print(p)
    
    print(len(outputimg))

# print(len(inputimg))

# part 1: 5204 low 5285 high