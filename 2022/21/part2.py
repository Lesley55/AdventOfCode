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

value = []
def equal(humn):
    monkey = copy.copy(inp)
    monkey["humn"] = humn / 1
    while not type(monkey["root"]) == float:
        for m in monkey:
            if not type(monkey[m]) == float:
                a = monkey[m].split()
                if type(monkey[a[0]]) == float and type(monkey[a[2]]) == float:
                    b = str(monkey[a[0]]) + a[1] + str(monkey[a[2]])
                    monkey[m] = eval(b)
    root = inp["root"].split()
    value.append(monkey[a[0]])
    return monkey[root[0]] == monkey[root[2]]

# printing root, the second value is always constant: 13439547545467
# and the first value is slowly decreasing when humn gets higher
# with almost a linear difference between values arround -7:1
# using this to get closer fast
humn = 0
for i in range(5):
    equal(humn)
    equal(humn + 1)
    diff = value[-1] - value[-2]
    humn += int((value[-1] - 13439547545467) / abs(diff))

while True:
    if equal(humn):
        break
    humn += 1

print(humn)
# part 2: 3952673930912
