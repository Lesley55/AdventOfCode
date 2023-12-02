input = open("input.txt")

total = 0

for i in input:
    i = i.replace(":", "").replace(";", "").replace(",", "").split()[2:]
    cubes = {"red": 0, "blue": 0, "green": 0}
    for j in range(0, len(i), 2):
        if int(i[j]) > cubes[i[j+1]]:
            cubes[i[j+1]] = int(i[j])
    total += cubes["red"] * cubes["blue"] * cubes["green"]

print(total)

# part 2: 69110
