input = open("input.txt")
input = input.readlines()

registers = {"a": 1, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0}
instructions = []
for i in input:
    instructions.append(i.strip().split(" "))

def getValue(a):
    if not a.isalpha():
        return int(a)
    else:
        return registers[a]

jump = 0
invoked = 0
# while True:
for i in range(50):
    if registers["d"] >= 2 and registers["e"] == 2 and jump == 11:
        # print(jump, instructions[jump], "e")
        registers["e"] += 107898
        registers["g"] = 0
        jump = 19
    elif registers["d"] == 2 and registers["e"] == 107900 and jump == 20:
        # print(jump, instructions[jump], "d")
        registers["d"] += 107897
        jump = 30 # :(
    if jump < 0 or jump >= len(instructions):
        break
    if instructions[jump][0] == "set":
        registers[instructions[jump][1]] = getValue(instructions[jump][2])
    elif instructions[jump][0] == "sub":
        registers[instructions[jump][1]] -= getValue(instructions[jump][2])
    elif instructions[jump][0] == "mul":
        invoked += 1
        registers[instructions[jump][1]] *= getValue(instructions[jump][2])
    elif instructions[jump][0] == "jnz":
        if getValue(instructions[jump][1]) != 0:
            print(jump, instructions[jump], registers)
            jump += getValue(instructions[jump][2])
            continue
    print(jump, instructions[jump], registers)
    jump += 1

print(registers["h"])

# part 2: 
