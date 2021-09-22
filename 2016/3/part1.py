input = open("input.txt")

possible = 0

for i in input:
    tri = i.split()
    for t in range(3):
        tri[t] = int(tri[t])
    tri.sort()
    if tri[0] + tri[1] > tri[2]:
        possible += 1

print(possible)

# part 1: 983