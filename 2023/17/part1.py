input = open("input.txt")
input = input.readlines()
for i in range(len(input)):
    input[i] = input[i].replace("\n", "")

pos = [[0, 0, 0, 0, -1, -1]]
end = [len(input) - 1, len(input[-1]) - 1]
min_loss = 999999999999999999999999999999
history = []
while 0 < len(pos):
    p = pos.pop(0)

    prev = False
    for i in range(len(history)):
        if history[i][:2] == p[:2] and history[i][-2:] == p[-2:] and history[i][3] <= p[3] and history[i][2] <= p[2]:
            prev = True
            break
    if prev:
        continue
    history.append(p)

    for i in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        new = [p[0] + i[0], p[1] + i[1]]
        if new != p[-2:] and 0 <= new[0] and new[0] < len(input) and 0 <= new[1] and new[1] < len(input[0]):
            straight = p[3]
            if [p[0] - i[0], p[1] - i[1]] != p[-2:]:
                straight = 0
            if straight < 3:
                loss = p[2] + int(input[new[0]][new[1]])
                if new == end:
                    if loss < min_loss:
                        min_loss = loss
                        pos = []
                elif loss < min_loss:
                    pos.append([p[0] + i[0], p[1] + i[1], loss, straight + 1] + p[:2])
                    pos.sort(key = lambda x: (x[2], -(x[0] + x[1])))

print(min_loss)

# part 1: 814
