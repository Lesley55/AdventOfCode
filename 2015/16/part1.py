input = open("input.txt")
mf = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}

inp = []

for i in input:
    inp.append(i)
    
print(len(inp))

for p in range(10): # i think it skips 1 when removing a sue, so just to be sure, making multiple iterations
    for i in inp:
        j = i.replace(":", "").replace(",", "").split()
        for m in mf:
            if (m == j[2] and mf[m] <= int(j[3])) or (m == j[4] and mf[m] <= int(j[5])) or (m == j[6] and mf[m] <= int(j[7])):
                if i in inp:
                    inp.remove(i)

print(len(inp))
print(inp)

# part 1: guessed 430 to high