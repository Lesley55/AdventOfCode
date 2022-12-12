input = open("input.txt")

start = ()
map = []
for i in input:
    i = i.strip()
    map.append(i)
    for j in range(len(i)):
        if i[j] == "S":
            map[len(map) - 1] = map[len(map) - 1][:j] + "a" + map[len(map) - 1][j + 1:]
        elif i[j] == "E":
            start = (len(map) - 1, j)
            map[len(map) - 1] = map[len(map) - 1][:j] + "z" + map[len(map) - 1][j + 1:]

import string
alphabet = string.ascii_lowercase
new = {start: 0}
prev = {}
while len(new) > 0:
    p = list(new.keys())[0]
    prev[p] = new.pop(p)
    for s in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        pos = (p[0] + s[0], p[1] + s[1])
        if pos[0] >= 0 and pos[0] < len(map) and pos[1] >= 0 and pos[1] < len(map[0]):
            if not pos in prev:
                if alphabet.index(map[pos[0]][pos[1]]) >= alphabet.index(map[p[0]][p[1]]) - 1:
                    new[pos] = prev[p] + 1

least = []
for i in prev:
    if map[i[0]][i[1]] == "a":
        least.append(prev[i])

print(sorted(least)[0])
# part 2: 321
