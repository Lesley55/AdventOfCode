input = 1358

def isOpen(x, y):
    number = (x * x) + (3 * x) + (2 * x * y) + y + (y * y)
    number += input
    binary = bin(number)
    one = 0
    for b in binary:
        if b == "1":
            one += 1
    return one % 2 == 0

visited = {}
possible = []
destination = False

def rec(x, y, steps):
    global destination

    # dont visit multiple times, which could create loops
    if (x,y) in visited or x < 0 or y < 0:
        return

    if steps == 51:
        destination = True
        return
    
    # add to visited
    visited[(x,y)] = True

    steps += 1
    # check if possible to set a step for every direction
    if isOpen(x+1, y):
        possible.append([x+1, y, steps])
    if isOpen(x, y+1):
        possible.append([x, y+1, steps])
    if isOpen(x-1, y):
        possible.append([x-1, y, steps])
    if isOpen(x, y-1):
        possible.append([x, y-1, steps])

rec(1, 1, 0) # starting point
while not destination:
    for i in possible:
        rec(i[0], i[1], i[2])

print(len(visited))

# part 2: 141
