input = open("input.txt")

total = 0
cubes = {"red": 12, "blue": 14, "green": 13}

for i in input:
    i = i.replace(":", "").replace(";", "").replace(",", "").split()
    game = int(i[1])
    i = i[2:]
    possible = True
    for j in range(0, len(i[2:]), 2):
        if int(i[j]) > cubes[i[j+1]]:
            possible = False
            break
    if possible:
        total += game

print(total)

# part 1: 2810
