input = open("input.txt")

lights = []
for i in input:
    lights.append(i.strip("\n"))

for n in range(100):
    new = []
    for m in range(100):
        new.append([])
    
    for i in range(len(lights)):
        for j in range(len(lights[i])):
            adjecent = 0
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if 0 <= i+k and i+k < len(lights) and 0 <= j+l and j+l < len(lights[i]):
                        if lights[i+k][j+l] == "#":
                            adjecent += 1
            if lights[i][j] == "#":
                adjecent -= 1
                if adjecent == 2 or adjecent == 3:
                    new[i].append("#")
                else:
                    new[i].append(".")
            elif lights[i][j] == ".":
                if adjecent == 3:
                    new[i].append("#")
                else:
                    new[i].append(".")
    lights = new

on = 0
for i in lights:
    for j in i:
        if j == "#":
            on += 1
print(on)

# part 1: 814