input = open("input.txt")
mf = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}

inp = []

for i in input:
    j = i.replace("\n", "").replace(":", "").replace(",", "").split()
    three = 0
    if j[2] in mf:
        if j[2] in ["cats", "trees"]:
            if int(j[3]) > mf[j[2]]:
                three += 1
        elif j[2] in ["pomeranians", "goldfish"]:
            if int(j[3]) < mf[j[2]]:
                three += 1
        else:
            if int(j[3]) == mf[j[2]]:
                three += 1
    if j[4] in mf:
        if j[4] in ["cats", "trees"]:
            if int(j[5]) > mf[j[4]]:
                three += 1
        elif j[4] in ["pomeranians", "goldfish"]:
            if int(j[5]) < mf[j[4]]:
                three += 1
        else:
            if int(j[5]) == mf[j[4]]:
                three += 1
    if j[6] in mf:
        if j[6] in ["cats", "trees"]:
            if int(j[7]) > mf[j[6]]:
                three += 1
        elif j[6] in ["pomeranians", "goldfish"]:
            if int(j[7]) < mf[j[6]]:
                three += 1
        else:
            if int(j[7]) == mf[j[6]]:
                three += 1

    if three == 3:
        print(j[1])

# part 2: 241