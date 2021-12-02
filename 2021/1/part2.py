input = open("input.txt")

depth = []
for i in input:
    depth.append(int(i))

sums = []
for i in range(2, len(depth)):
    sums.append(depth[i-2] + depth[i-1] + depth[i])

larger = 0
for i in range(1, len(sums)):
    if sums[i] > sums[i-1]:
        larger += 1

print(larger)

# part 2: 1618