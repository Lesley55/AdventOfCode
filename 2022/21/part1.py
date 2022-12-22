input = open("input.txt")

monkey = {}
for i in input:
    i = i.strip()
    i = i.split(": ")
    if i[1].isdigit():
        monkey[i[0]] = int(i[1]) / 1
    else:
        monkey[i[0]] = i[1]

while not type(monkey["root"]) == float:
    for m in monkey:
        if not type(monkey[m]) == float:
            a = monkey[m].split()
            if type(monkey[a[0]]) == float and type(monkey[a[2]]) == float:
                b = str(monkey[a[0]]) + a[1] + str(monkey[a[2]])
                monkey[m] = eval(b)

print(int(monkey["root"]))
# part 1: 54703080378102
