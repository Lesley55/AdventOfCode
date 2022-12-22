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
    # print(monkey[root[0]], monkey[root[2]])
    return monkey[root[0]] == monkey[root[2]]

humn = 3952673930000
while True:
    monkey = copy.copy(inp)
    monkey["humn"] = humn / 1
    if equal(monkey):
        break
    humn += 1

# printing root, the second value is always constant: 13439547545467
# and the first value is slowly decreasing when humn gets higher
# so i just put a random higher starting value for humn
# until i got close enough that running the code doesnt take ages
# would have preferred to code a solution, but at least i got the answer

print(humn)
# part 2: 3952673930912
