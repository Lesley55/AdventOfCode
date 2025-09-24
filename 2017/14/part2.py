def day10part2(input):
    a = []
    for i in input:
        a.append(ord(i))
    input = a + [17, 31, 73, 47, 23]

    hashlist = [i for i in range(256)]
    current = 0
    skip_size = 0

    for round in range(64):
        for i in range(len(input)):
            end = current + input[i]
            wrap_around = 0
            if end > len(hashlist) - 1:
                wrap_around  = end - len(hashlist)
            sub = hashlist[current:end] + hashlist[0:wrap_around]
            reverse = sub[::-1]
            hashlist = reverse[len(reverse) - wrap_around:] + hashlist[wrap_around:current] + reverse[:len(reverse)-wrap_around] + hashlist[end:]
            current += input[i] + skip_size
            current %= len(hashlist)
            skip_size += 1

    l = []
    while len(hashlist) > 1:
        b = hashlist[0]
        for i in range(1, 16):
            b = b ^ hashlist[i]
        l.append(b)
        hashlist = hashlist[16:]

    hash = ""
    for i in l:
        h = hex(i)[2:]
        if len(h) == 1:
            h = "0" + h
        hash += h

    return hash

##########################################################################

input = "oundnydw"

grid = []
for i in range(128):
    h = input + "-" + str(i)
    knothash = day10part2(h)

    row = ""
    for j in knothash:
        a = bin(int(j, 16))[2:]
        while len(a) < 4:
            a = "0" + a
        row += a
    grid.append(row)

regions = 0
visited = []

def check_neighbours(i, j):
    for x in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        pos = [i + x[0], j + x[1]]
        if 0 <= pos[0] and pos[0] < 128 and 0 <= pos[1] and pos[1] < 128:
            if not pos in visited:
                visited.append(pos)
                if grid[pos[0]][pos[1]] == "1":
                    check_neighbours(pos[0], pos[1])

for i in range(128):
    for j in range(128):
        if not [i, j] in visited:
            visited.append([i, j])
            if grid[i][j] == "1":
                regions += 1
                check_neighbours(i, j)

print(regions)

# part 2: 1164
