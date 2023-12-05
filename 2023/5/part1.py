input = open("input.txt")
input = input.readlines()

seeds = input[0].split()[1:]

for i in range(len(input)):
    if "map:" in input[i]:
        new_seeds = [i for i in seeds]
        for j in input[i+1:]:
            if j == "\n":
                break
            k = j.split()
            for s in range(len(seeds)):
                if int(k[1]) <= int(seeds[s]) and int(seeds[s]) < int(k[1]) + int(k[2]):
                    new_seeds[s] = int(k[0]) + int(seeds[s]) - int(k[1])
        seeds = new_seeds

print(min(seeds))

# part 1: 825516882
