input = open("input.txt")
input = input.readlines()

infected = {}
for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == "#":
            infected[(i, j)] = True

x = int(len(input) / 2)
y = int(len(input[0].strip()) / 2)
directions = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "W": (0, -1)}
direction = "N"
total = 0
for i in range(10000):
    if (x, y) in infected:
        if direction == "N":
            direction = "E"
        elif direction == "E":
            direction = "S"
        elif direction == "S":
            direction = "W"
        elif direction == "W":
            direction = "N"
        infected.pop((x, y))
    else:
        if direction == "N":
            direction = "W"
        elif direction == "W":
            direction = "S"
        elif direction == "S":
            direction = "E"
        elif direction == "E":
            direction = "N"
        infected[(x, y)] = True
        total += 1
    x += directions[direction][0]
    y += directions[direction][1]


print(total)

# part 1: 5176
