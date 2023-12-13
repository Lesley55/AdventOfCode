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
                for o in options[input[connection[0] + p[0]][connection[1] + p[1]]]:
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

def is_loop(i, j):
    if i % 1 == 0 and j % 1 == 0:
        if [i, j] in prev:
            return True
        else:
            return False
    connects = 0
    for n in [[-0.5, 0], [0.5, 0], [0, -0.5], [0, 0.5]]:
        if [i + n[0], j + n[1]] in prev:
            for o in options[input[int(i + n[0])][int(j + n[1])]]:
                if [i, j] == [i + n[0] + (o[0] / 2), j + n[1] + (o[1] / 2)]:
                    connects += 1
    if connects == 0:
        return False
    return True

for i in range(len(prev)):
    prev[i] = [float(prev[i][0]), float(prev[i][1])]

outside = []
inside = []
for i in range(len(input)):
    for j in range(len(input[i])):
        adj = [[i,j]]
        more = False
        while True:
            more = False
            for k in adj:
                if not (k in outside or k in inside or k in prev):
                    for l in [[-0.5, 0], [0.5, 0], [0, -0.5], [0, 0.5]]:
                        m = [k[0]+l[0], k[1]+l[1]]
                        if m[0] < 0 or len(input) <= m[0] or m[1] < 0 or len(input[i]) <= m[1] or m in outside:
                            outside += adj
                            break
                        elif m in inside:
                            inside += adj
                            break
                        elif not is_loop(m[0], m[1]) and not m in adj:
                            adj.append(m)
                            more = True
                    else:
                        continue
                    break
                else:
                    break
            else:
                if not more:
                    inside += adj
                    break
                continue
            break

total = 0
for i in inside:
    if i[0] % 1 == 0 and i[1] % 1 == 0:
        total += 1

print(total)

# part 2: 395
