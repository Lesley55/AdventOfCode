input = open("input.txt").readline()

for i in range(len(input)):
    distinct = set([*input[i:i+4]])
    if len(distinct) == 4:
        print(i+4)
        break

# part 1: 1343
