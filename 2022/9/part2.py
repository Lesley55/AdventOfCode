input = open("input.txt")

rope = [(0,0) for i in range(10)]

distinct = set()
for i in input:
    i = i.strip().split()
    step = {"R": [0, 1], "L": [0, -1], "U": [-1, 0], "D": [1, 0]}
    for j in range(int(i[1])):
        rope[0] = [rope[0][0] + step[i[0]][0], rope[0][1] + step[i[0]][1]]
        for k in range(1, len(rope)):
            d0, d1 = rope[k - 1][0] - rope[k][0], rope[k - 1][1] - rope[k][1]
            if (abs(d0) > 1 and d1 == 0) or (abs(d1) > 1 and d0 == 0) or (abs(d0) > 1 and abs(d1) > 1):
                rope[k] = (int(rope[k][0] + (d0 / 2)), int(rope[k][1] + (d1 / 2)))
            elif abs(d0) > 1:
                rope[k] = (int(rope[k][0] + (d0 / 2)), int(rope[k][1] + d1))
            elif abs(d1) > 1:
                rope[k] = (int(rope[k][0] + d0), int(rope[k][1] + (d1 / 2)))
        distinct.add(rope[-1])

print(len(distinct))
# part 2: 2445
