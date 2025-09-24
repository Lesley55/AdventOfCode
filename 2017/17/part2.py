input = 380
input = 3

buffer = [0]

p = 0
# for i in range(1, 50000001):
for i in range(1, 10):
    pos = buffer.index(i-1)
    stepstotake = input + 1
    toEnd = len(buffer) - pos
    if stepstotake > toEnd:
        pos = 0
        stepstotake -= toEnd
    if stepstotake > len(buffer):
        stepstotake = stepstotake % len(buffer)
    pos += stepstotake

    if pos == 0:
        buffer.append(i)
    else:
        buffer.insert(pos, i)
    # if buffer[pos-1] == 0:
    #     # print(pos-p)
    #     print(i)

    print(buffer)

print(buffer[buffer.index(0) + 1])

# part 2: 
