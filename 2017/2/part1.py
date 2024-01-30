input = open("input.txt")

total = 0
for i in input:
    i = i.split()
    i = list(map(int, i))
    total += max(i) - min(i)

print(total)

# part 1: 43074
