input = open("input.txt")

instructions = []
register = {}
for i in input:
    i = i.replace("inc", "+=")
    i = i.replace("dec", "-=")
    i = i.split()
    register[i[0]] = 0
    register[i[4]] = 0
    i[0] = "register[\"" + i[0] + "\"]"
    i[4] = "register[\"" + i[4] + "\"]"
    i = " ".join(i[3:]) + ":\n   " + " ".join(i[:3])
    instructions.append(i)

highest = 0
for i in instructions:
    exec(i)
    m = max(register.values())
    if m > highest:
        highest = m

print(highest)

# part 2: 6209
