input = open("input.txt")

total = 0
for i in input:
    i = i.split()
    valid = True
    for j in range(len(i)):
        for k in range(j + 1, len(i)):
            if i[j] == i[k]:
                valid = False
    if valid:
        total += 1

print(total)

# part 1: 383
