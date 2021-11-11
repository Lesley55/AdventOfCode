input = open("input.txt")
inp = []
all = []
tri = []

possible = 0

for i in input:
    inp.append(i)

for i in range(3):
    for j in inp:
        all.append(j.split()[i])

for k in range(len(all)):
    all[k] = int(all[k])

for a in range(len(all)):
    if a % 3 == 0:    
        if a+2 < len(all):
            tri.append([all[a], all[a+1], all[a+2]])

for t in tri:
    t.sort()

for n in tri:
    if n[0] + n[1] > n[2]:
        possible += 1

print(possible)

# part 2: 1836
