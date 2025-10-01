input = open("input.txt")
input = input.readlines()

instructions = []
registers = {}
for i in input:
    r = i.strip().split(" ")
    if not r[1] in registers and r[1].isalpha():
        registers[r[1]] = 0
    instructions.append(r)

def getValue(a):
    if not a.isalpha():
        return int(a)
    else:
        return registers[a]
    
jump = 0
last = 0
while True:
    if jump < 0 or jump >= len(instructions):
        print("terminated")
        break
    if instructions[jump][0] == "snd":
        last = getValue(instructions[jump][1])
    elif instructions[jump][0] == "set":
        registers[instructions[jump][1]] = getValue(instructions[jump][2])
    elif instructions[jump][0] == "add":
        registers[instructions[jump][1]] += getValue(instructions[jump][2])
    elif instructions[jump][0] == "mul":
        registers[instructions[jump][1]] *= getValue(instructions[jump][2])
    elif instructions[jump][0] == "mod":
        registers[instructions[jump][1]] %= getValue(instructions[jump][2])
    elif instructions[jump][0] == "rcv":
        if getValue(instructions[jump][1]) != 0:
            break
    elif instructions[jump][0] == "jgz":
        if registers[instructions[jump][1]] > 0:
            jump += getValue(instructions[jump][2])
            continue
    jump += 1

print(last)

# part 1: 4601
