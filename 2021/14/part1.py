from collections import Counter

input = open("input.txt")
template = [char for char in "BSONBHNSSCFPSFOPHKPK"]
steps = 10

insert = {}
for i in input:
    i = i.strip().split(" -> ")
    insert[i[0]] = i[1]

for s in range(steps):
    new = []
    for i in range(len(template)-1):
        substr = template[i] + template[i+1]
        new.append(template[i])
        if substr in insert:
            new.append(insert[substr])
    new.append(template[-1])
    template = new

occ = Counter(template)
print(max(occ.values()) - min(occ.values()))

# part 1: 2740
