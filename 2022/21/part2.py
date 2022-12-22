import copy

input = open("input.txt")

inp = {}
for i in input:
    i = i.strip()
    i = i.split(": ")
    if i[1].isdigit():
        inp[i[0]] = int(i[1]) / 1
    else:
        inp[i[0]] = i[1]

def equal(monkey):
    while not type(monkey["root"]) == float:
        for m in monkey:
            if not type(monkey[m]) == float:
                a = monkey[m].split()
                if type(monkey[a[0]]) == float and type(monkey[a[2]]) == float:
                    b = str(monkey[a[0]]) + a[1] + str(monkey[a[2]])
                    monkey[m] = eval(b)
    root = inp["root"].split()
    return monkey[root[0]] == monkey[root[2]]

i = 0
while True:
    monkey = copy.copy(inp)
    monkey["humn"] = i / 1
    if equal(monkey):
        break
    i += 1

print(i)
# part 2: 
