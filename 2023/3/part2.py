input = open("input.txt")

total = 0
engine = []

for i in input:
    engine.append(i.replace("\n", ""))

for i in range(len(engine)):
    for j in range(len(engine[i])):
        if engine[i][j] == "*":
            digits = []
            numbers = []
            for k in [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]:
                if 0 <= i+k[0] and i+k[0] < len(engine) and 0 <= j+k[1] and j+k[1] < len(engine[i+k[0]]):
                    if engine[i+k[0]][j+k[1]].isdigit() and not [i+k[0], j+k[1]] in digits:
                        l = [j+k[1], j+k[1]]
                        while 0 < l[0]:
                            if engine[i+k[0]][l[0]-1].isdigit():
                                l[0] -= 1
                                digits.append([i+k[0], l[0]])
                            else:
                                break
                        while l[1] < len(engine[i+k[0]]) - 1:
                            if engine[i+k[0]][l[1]+1].isdigit():
                                l[1] += 1
                                digits.append([i+k[0], l[1]])
                            else:
                                break
                        numbers.append(engine[i+k[0]][l[0]:l[1]+1])
            if len(numbers) == 2:
                total += int(numbers[0]) * int(numbers[1])

print(total)

# part 2: 77509019
