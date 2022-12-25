input = open("input.txt")

inp = []
for i in input:
    i = i.strip()
    inp.append(int(i))

c = {}
for i in range(len(inp) - 1):
    c[inp[i]] = (inp[i - 1], inp[i + 1])
c[inp[-1]] = (inp[-2], inp[0])

for i in inp:
    current = i
    # remove current
    c[c[i][0]] = (c[c[i][0]][0], c[i][1])
    c[c[i][1]] = (c[i][0], c[c[i][1]][1])
    # move
    for j in range(abs(i)):
        if i < 0:
            current = c[current][0] # prev
        else:
            current = c[current][1] # next
    if i <= 0:
        current = c[current][0] # prev
    # insert after current
    c[i] = (current, c[current][1])
    c[c[current][1]] = (i, c[c[current][1]][1])
    c[current] = (c[current][0], i)

sum = 0
after = 0
for i in range(1, 3001):
    after = c[after][1]
    if i % 1000 == 0:
        sum += after

print(sum)
# part 1: -2792 wrong