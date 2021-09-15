input = open("input.txt")

possible = 0

for i in input:
    tri = i.split()
    for t in range(len(tri)):
        tri[t] = int(tri[t])
    tri.sort()
    if int(tri[0]) + int(tri[1]) > int(tri[2]):
        possible += 1

print(possible)

# part 1: 983