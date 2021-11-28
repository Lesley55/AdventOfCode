import math

input = 3001330

elves = []

for i in range(input):
    elves.append(i)

current = 0
while len(elves) > 1:
    l = len(elves)
    if current < l:
        opposite = current + math.floor(l / 2)
        if opposite >= l:
            opposite -= l
        elves.pop(opposite)
        if opposite > current:
            current += 1
    else:
        current = 0

print(elves[0] + 1)

# part 2: 1407007
