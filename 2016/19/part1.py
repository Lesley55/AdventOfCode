input = 3001330

elves = {}

for i in range(input):
    elves[i] = True

current = 0
next = current + 1
while len(elves) > 1:
    if current < input:
        if current in elves:
            if next < input:
                if next in elves and next != current:
                    elves.pop(next)
                    current = next + 1
                    next = current + 1
                else:
                    next += 1
            else:
                next = 0
        else:
            current += 1
    else:
        current = 0

print(elves)
print("+1 because elves start from 1 not 0")

# part 1: 1808357
