input = open("input.txt")
input = input.readlines()
for i in range(len(input)):
    input[i] = input[i].replace("\n", "")
input[0] = "##" + input[0][2:]

pos = [[1, 1, 2, []]]
end = [len(input) - 1, len(input[-1]) - 2]
d = {">": [0, 1], "<": [0, -1], "v": [1, 0], "^": [-1, 0]}
longest = 0
while 0 < len(pos):
    p = pos.pop(0)
    for i in d:
        if input[p[0]][p[1]] in d and i != input[p[0]][p[1]]:
            continue
        new = [p[0] + d[i][0], p[1] + d[i][1]]
        if new == end:
            if longest < p[2]:
                longest = p[2]
            continue
        if input[new[0]][new[1]] != "#" and not new in p[3]:
            pos.append([new[0], new[1], p[2] + 1, [p[:2]] + p[3]])

print(longest)

# part 1: 2414
