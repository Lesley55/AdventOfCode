input = open("input.txt")

total = 0

for i in input:
    j = i[:-1]
    k = eval(i)
    total += len(j) - len(k)

print(total)

# part 1: 1342