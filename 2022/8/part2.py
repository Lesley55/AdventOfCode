input = open("input.txt")

trees = []
for i in input:
    i = i.strip()
    trees.append([*i])

max = 0

neighbor = [[0,1], [0,-1], [1,0], [-1,0]]
for row in range(len(trees)):
    for tree in range(len(trees[row])):
        score = 1
        for n in neighbor:
            next = n
            side = 0
            while True:
                if row + next[0] < 0 or tree + next[1] < 0 or row + next[0] >= len(trees) or tree + next[1] >= len(trees[0]):
                    break # index out of range
                side += 1
                if int(trees[row][tree]) <= int(trees[row + next[0]][tree + next[1]]):
                    break
                next = [next[0]+n[0], next[1]+n[1]]
            score *= side
        if score > max:
            max = score

print(max)
# part 2: 
