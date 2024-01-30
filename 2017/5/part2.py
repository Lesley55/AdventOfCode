input = open("input.txt")

instr = []
for i in input:
    instr.append(int(i))

i = 0
steps = 0
while True:
    if i < 0 or i >= len(instr):
        break
    steps += 1
    if instr[i] >= 3:
        instr[i] -= 1
        i += instr[i] + 1
    else:
        instr[i] += 1
        i += instr[i] - 1

print(steps)

# part 2: 27720699
