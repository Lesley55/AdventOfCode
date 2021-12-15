import copy

input = open("input.txt")

grid = []
for i in input:
    i = i.strip()
    grid.append([int(char) for char in i])

lowest = 9999999999999999
def recursive(x, y, risk, prev):
    global lowest
    if y == len(grid) and x == len(grid[-1]):
        if risk < lowest:
            lowest = risk
        return
    
    previous = copy.copy(prev)
    previous.append([x,y])
    possible = [[x + 1, y], [x - 1, y], [x, y - 1], [x, y + 1]]
    for i in possible:
        if not [i[0], i[1]] in prev and 0 <= i[1] and i[1] < len(grid) and 0 <= i[0] and i[0] < len(grid[i[1]]):
            recursive(i[0], i[1], risk + grid[i[1]][i[0]], previous)

recursive(0, 0, 0, [])

print(lowest)

# part 1: 
