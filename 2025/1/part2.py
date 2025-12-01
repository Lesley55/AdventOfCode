input = open("input.txt")

total = 0
dial = 50

for i in input:
    if i[0] == "R":
        for i in range(int(i[1:])):
            dial += 1
            dial %= 100
            if dial == 0:
                total += 1
    elif i[0] == "L":
        for i in range(int(i[1:])):
            dial -= 1
            if dial < 0:
                dial += 100
            if dial == 0:
                total += 1

print(total)

# part 2: 5820
