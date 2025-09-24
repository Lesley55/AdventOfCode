input = 380

buffer = [0]

for i in range(1, 2018):
    pos = buffer.index(i-1)
    stepstotake = input + 1
    toEnd = len(buffer) - pos
    if stepstotake > toEnd:
        pos = 0
        stepstotake -= toEnd
    if stepstotake > len(buffer):
        stepstotake = stepstotake % len(buffer)
    pos += stepstotake

    buffer.insert(pos, i)

print(buffer[buffer.index(2017) + 1])

# part 1: 204
