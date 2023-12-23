input = open("input.txt")
input = input.readlines()
for i in range(len(input)):
    input[i] = input[i].replace("\n", "")
input[0] = "##" + input[0][2:]

pos = [[1, 1, 2, [], []]]
end = [len(input) - 1, len(input[-1]) - 2]
longest = 0
while 0 < len(pos):
    p = pos.pop(-1) # last first, let the longer arrays finish first, instead of keeping them in memory longer
    n = 0 # find if cross section
    for i in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        if input[p[0] + i[0]][p[1] + i[1]] != "#":
            n += 1
    for i in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        new = [p[0] + i[0], p[1] + i[1]]
        if new == end:
            if longest < p[2]:
                longest = p[2]
                print(longest)
            continue
        if input[new[0]][new[1]] != "#" and not new in p[3] and not new in p[4]:
            if 2 < n: # keep track of cross sections, then remove previous positions in between from history
                pos.append([new[0], new[1], p[2] + 1, [], [p[:2]] + p[4]])
            else:
                pos.append([new[0], new[1], p[2] + 1, [p[:2]] + p[3], p[4]])

print(longest)

# part 2: 
