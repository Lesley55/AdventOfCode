import itertools

input = []

for i in open("input.txt"):
    input.append(int(i))

minimum = 9999999999
combinations = 0
for L in range(0, len(input)+1):
    for subset in itertools.combinations(input, L):
        if sum(subset) == 150:
            if len(subset) < minimum:
                minimum = len(subset)
                combinations = 1
            elif len(subset) == minimum:
                combinations += 1

print(combinations)

# part 2: 17