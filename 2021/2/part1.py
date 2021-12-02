input = open("input.txt")

x, y = 0, 0
for i in input:
    i = i.split()
    if i[0] == "forward":
        x += int(i[1])
    elif i[0] == "down":
        y += int(i[1])
    elif i[0] == "up":
        y -= int(i[1])

print(x * y)

# part 1: 2039912
