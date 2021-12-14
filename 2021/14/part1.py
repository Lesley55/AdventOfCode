input = open("input.txt")
template = "BSONBHNSSCFPSFOPHKPK"
steps = 10 # part 1
steps = 40 # part 2

amount = {}
insert = {}
for i in input:
    i = i.strip().split(" -> ")
    amount[i[0]] = 0
    insert[i[0]] = [i[0][0]+i[1], i[1]+i[0][1]]

for i in range(len(template)-1):
    amount[template[i:i+2]] += 1

for s in range(steps):
    new = {}
    for i in amount:
        for j in insert[i]:
            if j in new:
                new[j] += amount[i]
            else:
                new[j] = amount[i]
    amount = new

start = template[:2]
for s in range(steps):
    start = insert[start][0]

occ = {}
occ[start[0]] = amount[start]
for i in amount:
    if i[1] in occ:
        occ[i[1]] += amount[i]
    else:
        occ[i[1]] = amount[i]

print(max(occ.values()) - min(occ.values()))

# part 1: 2740
# part 2: 2959788056211
