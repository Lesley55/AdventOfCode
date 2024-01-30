input = 325489

spiral = {}
y, x = 0, 0
spiral[(y, x)] = 1

steps = 0
found = False
while not found:
    for dir in [[0, 1], [-1, 0], [0, -1], [1, 0]]:
        if dir[0] == 0:
            steps += 1
        for i in range(steps):
            y += dir[0]
            x += dir[1]
            new = 0
            for adj in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
                if (y + adj[0], x + adj[1]) in spiral:
                    new += spiral[(y + adj[0], x + adj[1])]
            if new > input and not found:
                print(new)
                found = True
                break
            spiral[(y, x)] = new

# part 2: 330785
