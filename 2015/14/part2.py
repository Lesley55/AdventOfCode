input = open("input.txt")

reindeer = {}
s = []
points = {}

for i in input:
    j = i.split()
    reindeer[j[0]] = 0
    points[j[0]] = 0
    s.append([j[0], int(j[3]), int(j[6]), int(j[13])])

for i in range(2503):
    for j in s:
        if i < j[2] or i % (j[3] + j[2]) < j[2]:
            reindeer[j[0]] += j[1]
    
    lead = max(reindeer, key=reindeer.get)
    lead = reindeer[lead]
    for r in reindeer:
        if reindeer[r] == lead:
            points[r] += 1

furthest = 0
for i in points.items():
    if i[1] > furthest:
        furthest = i[1]

print(furthest)

# part 2: 1256