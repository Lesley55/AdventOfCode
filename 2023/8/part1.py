input = open("input.txt")
input = input.readlines()

lr = input[0]
ins = {}
for i in input[2:]:
    i = i.replace("(", "").replace(")", "").replace(",", "").split()
    ins[i[0]] = (i[2], i[3])

pos = "AAA"
steps = 0
l = len(lr) - 1

while pos != "ZZZ":
    if lr[steps % l] == "L":
        pos = ins[pos][0]
    else:
        pos = ins[pos][1]
    steps += 1

print(steps)

# part 1: 18827
