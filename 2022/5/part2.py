input = open("input.txt")

stacks = {}
for i in input:
    if "[" in i:
        for j in range(0, len(i) - 2, 4):
            k = int(j/4) + 1
            if not k in stacks:
                stacks[k] = []
            if i[j + 1] != " ":
                stacks[k].append(i[j + 1])
    elif "move" in i:
        i = i.strip().split(" ")
        sub = []
        for j in range(int(i[1])):
            sub.append(stacks[int(i[3])].pop(0))
        for j in sub[::-1]:
            stacks[int(i[5])].insert(0, j)

top = ""
for i in stacks:
    top += stacks[i][0]

print(top)
# part 2: GCFGLDNJZ
