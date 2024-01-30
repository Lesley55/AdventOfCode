input = open("input.txt")

total = 0
for i in input:
    i = i.split()
    i = list(map(int, i))
    for j in range(len(i)):
        for k in range(j + 1, len(i)):
            if i[j] % i[k] == 0:
                total += i[j] / i[k]
            if i[k] % i[j] == 0:
                total += i[k] / i[j]

print(int(total))

# part 2: 280
