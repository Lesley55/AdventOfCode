import itertools

input = []

for i in open("input.txt"):
    input.append(int(i))

combinations = 0
for L in range(0, len(input)+1):
    for subset in itertools.combinations(input, L):
        if sum(subset) == 150:
            combinations += 1

print(combinations)

# part 1: 1638