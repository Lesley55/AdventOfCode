input = open("input.txt")
input = input.readlines()

times = [int(i) for i in input[0].split()[1:]]
dist = [int(i) for i in input[1].split()[1:]]

total = 1

for race in range(len(times)):
    ways = 0
    for ms in range(times[race]):
        if ms * (times[race] - ms) > dist[race]:
            ways += 1
    total *= ways

print(total)

# part 1: 3316275
