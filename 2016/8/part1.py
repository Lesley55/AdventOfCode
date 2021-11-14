input = open("input.txt")

width = 50
height = 6

screen = []

# initialize screen
for i in range(height):
    pixels = []
    for j in range(width):
        pixels.append(False)
    screen.append(pixels)

# execure instructions
for i in input:
    arr = i.strip().split(' ')
    if arr[0] == "rect":
        w, h = arr[1].split('x')
        w = int(w)
        h = int(h)
        for hh in range(h):
            for ww in range(w):
                screen[hh][ww] = True
    elif arr[0] == "rotate":
        xy, a = arr[2].split('=')
        a = int(a)
        offset = arr[4]
        offset = int(offset)
        if arr[1] == "row":
            offset = width - offset
            screen[a] = screen[a][offset:] + screen[a][:offset]
        elif arr[1] == "column":
            column = []
            for i in screen:
                column.append(i[a])
            offset = height - offset
            column = column[offset:] + column[:offset]
            for i in range(len(screen)):
                screen[i][a] = column[i]

# count pixels
total = 0
for i in screen:
    for j in i:
        if j:
            total += 1
print(total)

# part 2
for i in range(height):
    for j in range(width):
        if screen[i][j]:
            screen[i][j] = "#"
        else:
            screen[i][j] = "."
    screen[i] = "".join(screen[i])
    print(screen[i])

# part 1: 123
# part 2: afbupzbjps