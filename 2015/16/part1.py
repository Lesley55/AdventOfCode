input = open("input.txt")
mf = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}

inp = []

for i in input:
    inp.append(i)
    
print(len(inp))

i = 0
while i < len(inp):
    j = inp[i].replace(":", "").replace(",", "").split()
    for m in mf:
        if (m == j[2] and mf[m] > int(j[3])) or (m == j[4] and mf[m] > int(j[5])) or (m == j[6] and mf[m] > int(j[7])):
            inp.remove(inp[i])
            i -= 1
            break
    i += 1

print(len(inp))
print(inp)

# part 1: guessed 430 to high