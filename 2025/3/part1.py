input = open("input.txt")

total = 0

for i in input:
    row = []
    for j in i.strip():
        row.append(int(j))
    k = max(row[:-1])
    ki = row.index(k)
    row = row[ki+1:]
    l = max(row)
    joltage = str(k) + str(l)
    total += int(joltage)

print(total)

# part 1: 17144
