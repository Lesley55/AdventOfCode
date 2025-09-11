input = open("input.txt")
input = input.readlines()

programs = {}
for i in input:
    i = i.strip().split(" <-> ")
    programs[i[0]] = i[1].split(", ")

visited = []
check = ['0']

while len(check) > 0:
    current = check.pop(0)
    if current in visited:
        continue
    visited.append(current)
    for i in programs[current]:
        if not i in visited and not i in check:
            check.append(i)

print(len(visited))

# part 1: 380
