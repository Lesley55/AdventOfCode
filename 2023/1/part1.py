input = open("input.txt")

total = 0

for i in input:
    d = ""
    for j in i:
        if j.isdigit():
            d += j
    print(d[0]+d[-1])
    total += int(d[0]+d[-1])

print(total)

# part 1: 55029
