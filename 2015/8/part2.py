input = open("input.txt")

total = 0

for i in input:
    j = i.count("\\")
    k = i.count("\"")
    total += 2 + j + k

print(total)

# part 2: 2074