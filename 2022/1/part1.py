input = open("input.txt")

calories = []
elf = []
for i in input:
    i = i.strip()
    if i != "":
        elf.append(int(i))
    else:
        calories.append(sum(elf))
        elf = []
calories.append(sum(elf))

print(max(calories))
# part 1: 71924

calories.sort()
print(sum(calories[-3:]))
# part 2: 210406
