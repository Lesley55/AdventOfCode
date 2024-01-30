input = open("input.txt")
input = input.readline().split()
input = list(map(int, input))

history = {}
cycles = 0
while True:
    if tuple(input) in history:
        break
    history[tuple(input)] = cycles
    cycles += 1
    m = max(input)
    index = input.index(m)
    input[index] = 0
    for i in range(index + 1, index + m + 1):
        input[i % len(input)] += 1

print(cycles - history[tuple(input)])

# part 2: 2793
