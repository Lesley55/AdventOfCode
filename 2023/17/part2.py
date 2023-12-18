input = open("input.txt")
input = input.readlines()
for i in range(len(input)):
    input[i] = input[i].replace("\n", "")

pos = [[0, 0, 0, 0, -1], [0, 0, 0, -1, 0]]
end = [len(input) - 1, len(input[-1]) - 1]
min_loss = float("inf")
history = []
while 0 < len(pos):
    p = pos.pop(0)

    prev = False
    for i in range(len(history)):
        if history[i][:2] == p[:2] and history[i][3:] == p[3:] and history[i][2] <= p[2]:
            prev = True
            break
    if prev:
        continue
    history.append(p)

    for i in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        if i[0] != abs(p[0] - p[3]) and i[1] != abs(p[1] - p[4]):
            for d in range(4, 11):
                new = [p[0] + (i[0] * d), p[1] + (i[1] * d)]
                if 0 <= new[0] and new[0] < len(input) and 0 <= new[1] and new[1] < len(input[0]):
                    loss = p[2]
                    for l in range(d):
                        loss += int(input[new[0] - (i[0] * l)][new[1] - (i[1] * l)])
                    if new == end:
                        if loss < min_loss:
                            min_loss = loss
                    elif loss < min_loss:
                        pos.append(new + [loss] + [new[0] - (i[0] * 2), new[1] - (i[1] * 2)])
                        pos.sort(key = lambda x: (x[2], -(x[0] + x[1])))

print(min_loss)

# part 2: 
