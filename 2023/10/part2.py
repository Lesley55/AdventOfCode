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

outside = []
inside = []
for i in range(len(input)):
    for j in range(len(input[i])):
        adj = [[i,j]]
        more = False
        while True:
            more = False
            for k in adj:
                if not (k in outside or k in inside):
                    for l in [[-0.5, 0], [0.5, 0], [0, -0.5], [0, 0.5]]:
                        m = [k[0]+l[0], k[1]+l[1]]
                        if m[0] < 0 or len(input) <= m[0] or m[1] < 0 or len(input[i]) <= m[1] or m in outside:
                            outside += adj
                            break
                        elif m in inside:
                            inside += adj
                            break
                        elif not m in prev:
                            # bug is probably here, gl debugging future self, time for sleep #############
                            connects = 0
                            for n in [[-0.5, 0], [0.5, 0], [0, -0.5], [0, 0.5]]:
                                if m[0] + n[0] % 1 == 0 and m[1] + n[1] % 1 == 0:
                                    if [int(m[0] + n[0]), int(m[1] + n[1])] in prev:
                                        for o in options[input[int(m[0] + n[0])][int(m[1] + n[1])]]:
                                            p = [m[0] + n[0] + (o[0] / 2), m[1] + n[1] + (o[1] / 2)]
                                            if p[0] % 1 != 0:
                                                p = [int(p[0]), p[1]]
                                            if p[1] % 1 != 0:
                                                p = [p[0], int(p[1])]
                                            if p == m:
                                                connects += 1
                            ###############################################################################
                            if not 1 < connects:
                                adj.append(m)
                                more = True
                    else:
                        continue
                    break
            else:
                if not more:
                    inside += adj
                    break
                continue
            break

print(len(outside), outside)
print(len(inside), inside)

# part 2: 
