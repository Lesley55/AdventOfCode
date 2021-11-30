input = open("input.txt")

cmd = []

for i in input:
    i = i.strip().split()
    cmd.append(i)

r = ["a", "b", "c", "d"]
registers = [12,0,0,0]

i = 0
while i < len(cmd):
    if cmd[i][0] == "cpy" and not cmd[i][2].lstrip("-").isdigit():
        if cmd[i][1].lstrip("-").isdigit():
            registers[r.index(cmd[i][2])] = int(cmd[i][1])
        else:
            registers[r.index(cmd[i][2])] = registers[r.index(cmd[i][1])]
    elif cmd[i][0] == "inc" and not cmd[i][1].lstrip("-").isdigit():
        registers[r.index(cmd[i][1])] += 1
    elif cmd[i][0] == "dec" and not cmd[i][1].lstrip("-").isdigit():
        registers[r.index(cmd[i][1])] -= 1
    elif cmd[i][0] == "jnz":
        zero = False
        if cmd[i][1].lstrip("-").isdigit():
            if cmd[i][1] == 0:
                zero = True
        elif registers[r.index(cmd[i][1])] == 0:
                zero = True
        if not zero:
            if cmd[i][2].lstrip("-").isdigit():
                i += int(cmd[i][2])
            else:
                i += registers[r.index(cmd[i][2])]
            continue
    elif cmd[i][0] == "tgl":
        a = None
        if cmd[i][1].lstrip("-").isdigit():
            a = int(cmd[i][1])
        else:
            a = registers[r.index(cmd[i][1])]
        
        if 0 <= i+a and i+a < len(cmd):
            if len(cmd[i+a]) == 2:
                if cmd[i+a][0] == "inc":
                    cmd[i+a][0] = "dec"
                else:
                    cmd[i+a][0] = "inc"
            else:
                if cmd[i+a][0] == "jnz":
                    cmd[i+a][0] = "cpy"
                else:
                    cmd[i+a][0] = "jnz"
    i += 1

print(registers[r.index("a")])

# part 2: 479009223
