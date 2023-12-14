input = open("input.txt")
input = input.readlines()
for i in range(len(input)):
    input[i] = input[i].replace("\n", "")

roll = []
stuck = []
for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == "O":
            roll.append([i, j])
        if input[i][j] == "#":
            stuck.append([i, j])

history = []
cycle = 0
while cycle < 1000000000:
    cycle += 1
    for d in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
        if d == [-1, 0]:
            roll.sort(key = lambda x: x[0])
        elif d == [0, -1]:
            roll.sort(key = lambda x: x[1])
        elif d == [1, 0]:
            roll.sort(key = lambda x: -x[0])
        elif d == [0, 1]:
            roll.sort(key = lambda x: -x[1])
        changed = True
        while changed:
            changed = False
            for rock in range(len(roll)):
                moved = [roll[rock][0] + d[0], roll[rock][1] + d[1]]
                while 0 <= moved[0] and 0 <= moved[1] and moved[0] < len(input) and moved[1] < len(input[0]) and not moved in roll and not moved in stuck:
                    roll[rock] = moved
                    changed = True
                    moved = [moved[0] + d[0], moved[1] + d[1]]
    for h in history:
        if roll == h[1]:
            cycle = 1000000000 - ((1000000000 - h[0]) % (cycle - h[0]))
            history = []
            break
    else:
        history.append([cycle, [r for r in roll]])

total = 0

for rock in roll:
    total += len(input) - rock[0]

print(total)

# part 2: 104533
