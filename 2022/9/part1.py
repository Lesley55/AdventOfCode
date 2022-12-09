input = open("input.txt")

h = (0, 0)
t = (0, 0)
distinct = set()
for i in input:
    i = i.strip().split()
    step = {"R": [0, 1], "L": [0, -1], "U": [-1, 0], "D": [1, 0]}
    for j in range(int(i[1])):
        h = [h[0] + step[i[0]][0], h[1] + step[i[0]][1]]
        d0, d1 = h[0] - t[0], h[1] - t[1]
        if (abs(d0) > 1 and d1 == 0) or (abs(d1) > 1 and d0 == 0):
            t = (int(t[0] + (d0 / 2)), int(t[1] + (d1 / 2)))
        elif abs(d0) > 1:
            t = (int(t[0] + (d0 / 2)), int(t[1] + d1))
        elif abs(d1) > 1:
            t = (int(t[0] + d0), int(t[1] + (d1 / 2)))
        distinct.add(t)

print(len(distinct))
# part 1: 5902
