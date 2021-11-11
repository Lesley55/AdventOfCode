from itertools import permutations

input = open("input.txt")

people = set()
happy = []

for i in input:
    c = i.replace(".", "").split()
    people.add(c[0])
    if c[2] == "gain":
        happy.append([c[0], c[10], int(c[3])])
    elif c[2] == "lose":
        happy.append([c[0], c[10], int(c[3]) * -1])
        

best = 0

# loop all possible cominations
for comb in permutations(people):
    total = 0
    for j in range(len(comb)):
        for n in happy:
            if j + 1 == len(comb):
                if (comb[j] == n[0] and comb[0] == n[1]) or (comb[0] == n[0] and comb[j] == n[1]):
                    total += n[2]
            else:
                if (comb[j] == n[0] and comb[j+1] == n[1]) or (comb[j+1] == n[0] and comb[j] == n[1]):
                    total += n[2]
    if total > best:
        best = total

print(best)

# part 1: 664