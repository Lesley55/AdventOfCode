input = open("input.txt")
input = input.readlines()

pos = []
for i in range(len(input)):
    input[i] = input[i].replace("\n", "")
    for j in range(len(input[i])):
        if input[i][j] == "S":
            pos.append([i, j])

options = {"|": [[-1,0], [1,0]], "-": [[0,-1], [0,1]], "L": [[-1,0], [0,1]], "J": [[-1,0], [0,-1]], "7": [[0,-1], [1,0]], "F": [[0,1], [1,0]], ".": [], "S": [[-1,0], [1,0], [0,-1], [0,1]]}
new = []
prev = [] + pos
steps = 0
middle = False
while not middle:
    temp_prev = []
    for p in pos:
        for connection in options[input[p[0]][p[1]]]:
            if not [p[0] + connection[0], p[1] + connection[1]] in prev:
                connects = 0
                temp = []
                for o in options[input[connection[0] + p[0]][connection[1] + p[1]]]: #
                    if not [p[0] + connection[0] + o[0], p[1] + connection[1] + o[1]] in prev:
                        temp.append([p[0] + connection[0], p[1] + connection[1]])
                    else:
                        connects += 1
                if 1 < connects:
                    temp.append([p[0] + connection[0], p[1] + connection[1]])
                if 0 < connects:
                    new += temp
                    temp_prev.append([p[0] + connection[0], p[1] + connection[1]])
    prev += temp_prev
    temp_prev = []
    pos = new
    new = []
    steps += 1
    for i in pos:
        if pos.count(i) > 1:
            middle = True
            break

print(steps)

# part 1: 7012
