import copy

input = open("input.txt")
rocks = [
    [
        "####",
    ],
    [
        ".#.",
        "###",
        ".#.",
    ],
    [
        "..#",
        "..#",
        "###",
    ],
    [
        "#",
        "#",
        "#",
        "#",
    ],
    [
        "##",
        "##",
    ],
]

# turn rocks strings into positions
for r in range(len(rocks)):
    pos = []
    for i in range(len(rocks[r])):
        for j in range(len(rocks[r][i])):
            if rocks[r][len(rocks[r]) - 1 - i][j] == "#":
                pos.append((i, j))
    rocks[r] = pos

chamber = [["." for i in range(7)] for j in range(7)]
jet = input.readline()
rock = copy.copy(rocks[0])
for r in range(len(rock)):
    rock[r] = (rock[r][0] + 3, rock[r][1] + 2)

target = 1000000000000
# target = 2022
i = 0
jeti = 0

def remove_empty():
    global chamber
    for j in range(len(chamber)):
        if not "#" in chamber[j]:
            chamber = chamber[:j]
            break

landed_rocks = {}
units = 0
def find_pattern():
    global chamber, target, units, i, landed_rocks
    if len(chamber) > 20:
        for p in range(10, int(len(chamber) / 2)):
            same = True
            for q in range(p):
                if chamber[-q] != chamber[-p-q]:
                    same = False
                    break
            if same and len(chamber) - p in landed_rocks:
                fallen = landed_rocks[len(chamber)] - landed_rocks[len(chamber) - p]
                units = int(target / fallen) * p
                target = target % fallen
                return

def landed():
    global chamber, rock, i
    for r in rock:
        rpos = (r[0] - 1, r[1])
        if rpos[0] < 0 or chamber[rpos[0]][rpos[1]] == "#":
            # add rock to chamber
            for j in rock:
                chamber[j[0]][j[1]] = "#"
            # remove empty rows from chamber
            remove_empty()
            # next rock
            i += 1
            rock = copy.copy(rocks[i % len(rocks)])
            for r in range(len(rock)):
                rock[r] = (rock[r][0] + len(chamber) + 3, rock[r][1] + 2)
            # check for pattern to skip steps
            if units == 0:
                landed_rocks[len(chamber)] = i
                find_pattern()
            # add empty positions for checking if rock
            for j in range(7):
                chamber.append(["." for l in range(7)])
            return True
    return False

def left():
    global rock
    for r in range(len(rock)):
        rock[r] = (rock[r][0], rock[r][1] - 1)

def right():
    global rock
    for r in range(len(rock)):
        rock[r] = (rock[r][0], rock[r][1] + 1)

while i < target:
    # push side
    if jet[jeti % len(jet)] == "<":
        left()
        for r in rock:
            if r[1] < 0 or chamber[r[0]][r[1]] == "#":
                right()
                break
    else:
        right()
        for r in rock:
            if r[1] >= 7 or chamber[r[0]][r[1]] == "#":
                left()
                break
    jeti += 1
    # fall
    if landed():
        continue
    for r in range(len(rock)):
        rock[r] = (rock[r][0] - 1, rock[r][1])

remove_empty()
print(units + len(chamber))
# part 2: 
