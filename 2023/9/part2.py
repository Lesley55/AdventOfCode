input = open("input.txt")
input = input.readlines()

total = 0

for i in range(len(input)):
    pyramid = [[int(j) for j in input[i].split()]]
    while not list(set(pyramid[-1])) == [0]:
        diff = []
        for j in range(1, len(pyramid[-1])):
            diff.append(pyramid[-1][j] - pyramid[-1][j-1])
        pyramid.append(diff)
    history = 0
    for p in pyramid[::-1]:
        history = p[0] - history
    total += history

print(total)

# part 2: 1108
