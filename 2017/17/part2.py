input = 380
bufferLen = 1
pos = 0
lastAfterZero = 0

for i in range(1, 50000001):
    pos += input
    if pos >= bufferLen:
        pos = pos % bufferLen
    pos += 1
    if pos == 1:
        lastAfterZero = i
    bufferLen += 1

print(lastAfterZero)

# part 2: 28954211
