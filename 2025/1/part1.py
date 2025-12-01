input = open("input.txt")

total = 0
dial = 50

for i in input:
    if i[0] == "R":
        dial += int(i[1:])
        dial %= 100
    elif i[0] == "L":
        dial -= int(i[1:])
        while dial < 0:
            dial += 100
    if dial == 0:
        total += 1

print(total)

# part 1: 1007
