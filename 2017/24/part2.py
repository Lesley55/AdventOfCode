input = open("input.txt")
input = input.readlines()

components = []
for i in input:
    i = i.strip().split("/")
    i[0] = int(i[0])
    i[1] = int(i[1])
    components.append(i)

strongest = 0
length = 0

def r(options, bridge = []):
    global strongest, length
    last = 0 if len(bridge) <= 0 else bridge[-1]
    for o in range(len(options)):
        if last == options[o][0]:
            br = bridge.copy()
            br += options[o]
            op = options.copy()
            op.remove(options[o])
            r(op, br)
        elif last == options[o][1]:
            br = bridge.copy()
            br += options[o][::-1]
            op = options.copy()
            op.remove(options[o])
            r(op, br)
    strength = 0
    for b in bridge:
        strength += b
    if len(bridge) == length:
        if strength > strongest:
            strongest = strength
    if len(bridge) > length:
        length = len(bridge)
        strongest = strength

r(components)
print(strongest)

# part 2: 1994
