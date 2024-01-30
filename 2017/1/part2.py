input = open("input.txt")
input = input.readline()

total = 0
for i in range(len(input)):
    if input[i] == input[i - int(len(input)/2)]:
        total += int(input[i])

print(total)

# part 2: 1152
