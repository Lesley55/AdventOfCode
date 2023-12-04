input = open("input.txt")

total = 0

for i in input:
    i = i.replace("/n", "").split()
    winning = i[2:12]
    numbers = i[13:]
    points = 0
    for n in numbers:
        if n in winning:
            if 0 < points:
                points *= 2
            else:
                points += 1
    total += points

print(total)

# part 1: 25183
