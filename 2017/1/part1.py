input = open("input.txt")
input = input.readline()

total = 0
for i in range(len(input)):
    if input[i] == input[i - 1]:
        total += int(input[i])

print(total)

# part 1: 1182
