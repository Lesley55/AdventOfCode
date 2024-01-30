input = open("input.txt")

discs = {}
for i in input:
    i = i.split()
    s = []
    if 2 < len(i):
        for j in range(3, len(i)):
            s.append(i[j].replace(",",""))
    discs[i[0]] = [int(i[1][1:-1]), s]

found = False
def weight(d):
    global found
    a = [weight(s) for s in discs[d][1]]
    if 0 < len(a) and min(a) != max(a) and not found:
        print(discs[discs[d][1][a.index(max(a))]][0] - (max(a) - min(a)))
        found = True
    return discs[d][0] + sum(a)

w = weight("xegshds")

# part 2: 299
