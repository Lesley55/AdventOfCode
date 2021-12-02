input = open("input.txt")

depth = []
for i in input:
    depth.append(int(i))

larger = 0
for i in range(1, len(depth)):
    if depth[i] > depth[i-1]:
        larger += 1

print(larger)

# part 1: 1581