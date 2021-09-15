input = open("input.txt")

x = 0
y = 2
keypad = [
    [0, 0, 1, 0, 0],
    [0, 2, 3, 4, 0],
    [5, 6, 7, 8, 9],
    [0, "A", "B", "C", 0],
    [0, 0, "D", 0, 0],
]
code = ""

for i in input:
    for j in i:
        newX = x
        newY = y
        if j == "U":
            newY -= 1
        elif j == "D":
            newY += 1
        elif j == "R":
            newX += 1
        elif j == "L":
            newX -= 1

        if 0 <= newX and newX <= 4 and 0 <= newY and newY <= 4:
            if keypad[newY][newX] != 0:
                x = newX
                y = newY
    code += str(keypad[y][x])
print(code)

# part 2: 46C92
