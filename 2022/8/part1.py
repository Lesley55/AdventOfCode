input = open("input.txt")

trees = []
for i in input:
    i = i.strip()
    trees.append([*i])

visible = 2 * len(trees) + 2 * len(trees[0]) - 4

neighbor = [[0,1], [0,-1], [1,0], [-1,0]]
for row in range(1, len(trees) - 1):
    for tree in range(1, len(trees[row]) - 1):
        for n in neighbor:
            vis = True
            next = n
            while True:
                if int(trees[row][tree]) > int(trees[row + next[0]][tree + next[1]]):
                    next = [next[0]+n[0], next[1]+n[1]]
                    if row + next[0] < 0 or tree + next[1] < 0 or row + next[0] >= len(trees) or tree + next[1] >= len(trees[0]):
                        break # index out of range
                else:
                    vis = False
                    break
            if vis:
                visible += 1
                break

print(visible)
# part 1: 1794
