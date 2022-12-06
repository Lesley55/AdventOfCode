input = open("input.txt").readline()

for i in range(len(input)):
    distinct = set([*input[i:i+14]])
    if len(distinct) == 14:
        print(i+14)
        break

# part 2: 2193
