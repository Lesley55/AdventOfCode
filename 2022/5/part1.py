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
        for j in range(int(i[1])):
            stacks[int(i[5])].insert(0, stacks[int(i[3])].pop(0))

top = ""
for i in stacks:
    top += stacks[i][0]

print(top)
# part 1: VCTFTJQCG
