input = open("input.txt")

octo = {}
t = 0
for i in input:
    i = i.strip()
    for j in range(len(i)):
        octo[(t,j)] = int(i[j])
    t += 1

s = 0
while True:
    for i in octo:
        octo[i] += 1

    flashed = []
    f = True
    while f:
        f = False
        for i in octo:
            if octo[i] > 9 and not i in flashed:
                f = True
                flashed.append(i)
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        if (i[0]+l, i[1]+k) in octo:
                            octo[(i[0]+l, i[1]+k)] += 1
    
    all = True
    for i in octo:
        if octo[i] > 9:
            octo[i] = 0
        else:
            all = False

    s += 1
    if all:
        break

print(s)

# part 2: 364
