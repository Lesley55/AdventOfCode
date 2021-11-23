input = open("input.txt")

cmd = []

for i in input:
    i = i.strip().split()
    cmd.append(i)

r = ["a", "b", "c", "d"]
registers = [0,0,1,0]

i = 0
while i < len(cmd):
    if cmd[i][0] == "cpy":
        if cmd[i][1].isnumeric():
            registers[r.index(cmd[i][2])] = int(cmd[i][1])
        else:
            registers[r.index(cmd[i][2])] = registers[r.index(cmd[i][1])]
    elif cmd[i][0] == "inc":
        registers[r.index(cmd[i][1])] += 1
    elif cmd[i][0] == "dec":
        registers[r.index(cmd[i][1])] -= 1
    elif cmd[i][0] == "jnz":
        zero = False
        if cmd[i][1].isnumeric():
            if cmd[i][1] == 0:
                zero = True
        elif registers[r.index(cmd[i][1])] == 0:
                zero = True
        if not zero:
            i += int(cmd[i][2])
            continue
    i += 1

print(registers[r.index("a")])

# part 2: 9227663
