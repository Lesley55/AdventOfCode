input = open("input.txt")
steps = 100

octo = {}
t = 0
for i in input:
    i = i.strip()
    for j in range(len(i)):
        octo[(t,j)] = int(i[j])
    t += 1

total = 0
for s in range(steps):
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
                total += 1
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        if (i[0]+l, i[1]+k) in octo:
                            octo[(i[0]+l, i[1]+k)] += 1
    
    for i in octo:
        if octo[i] > 9:
            octo[i] = 0

print(total)

# part 1: 
