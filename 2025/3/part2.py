input = open("input.txt")

total = 0

for i in input:
    row = []
    for j in i.strip():
        row.append(int(j))
    row.append(0)
    joltage = ""
    while len(joltage) < 12:
        k = max(row[:-12+len(joltage)])
        ki = row.index(k)
        joltage += str(k)
        row = row[ki+1:]
    total += int(joltage)

print(total)

# part 2: 170371185255900
