input = open("input.txt")
input = input.readlines()

layers = []
for i in input:
    layer = i.strip().split(": ")
    layer = [int(layer[0]), int(layer[1])]
    layers.append(layer)

delay = 0
while True:
    caught = False
    for l in layers:
        cycle = l[1] * 2 - 2
        if (l[0] + delay) % cycle == 0:
            caught = True
            delay += 1
            break
    if not caught:
        break

print(delay)

# part 2: 3849742
