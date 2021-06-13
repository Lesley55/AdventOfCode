input = open("input.txt")
mf = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}

inp = []

for i in input:
    j = i.replace("\n", "").replace(":", "").replace(",", "").split()
    if j[2] in mf and int(j[3]) == mf[j[2]] and j[4] in mf and int(j[5]) == mf[j[4]] and j[6] in mf and int(j[7]) == mf[j[6]]:
        print(j[1])

# part 1: 40