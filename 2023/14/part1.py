input = open("input.txt")
input = input.readlines()

roll = []
stuck = []
for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == "O":
            roll.append([i, j])
        if input[i][j] == "#":
            stuck.append([i, j])

changed = True
while changed:
    changed = False
    for rock in range(len(roll)):
        up = [roll[rock][0] - 1, roll[rock][1]]
        if 0 <= up[0] and not up in roll and not up in stuck:
            roll[rock] = up
            changed = True

total = 0

for rock in roll:
    total += len(input) - rock[0]

print(total)

# part 1: 108813
