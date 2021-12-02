input = open("input.txt")

x, y, aim = 0, 0, 0
for i in input:
    i = i.split()
    if i[0] == "forward":
        x += int(i[1])
        y += int(i[1]) * aim
    elif i[0] == "down":
        aim += int(i[1])
    elif i[0] == "up":
        aim -= int(i[1])

print(x * y)

# part 2: 1942068080
