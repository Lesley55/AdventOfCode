input = open("input.txt")

x = 1
cycle = 0
v = {}
crt = ["" for i in range(6)]

def check():
    global x, cycle, v
    if cycle in v:
        x += v.pop(cycle)
    if cycle % 40 in [x - 1, x, x + 1]:
        crt[int(cycle / 40)] += "#"
    else:
        crt[int(cycle / 40)] += "."
    cycle += 1

for i in input:
    i = i.strip().split()
    if i[0] == "addx":
        if cycle + 2 in v:
            v[cycle + 2] += int(i[1])
        else:
            v[cycle + 2] = int(i[1])
            check()
    check()

for i in crt:
    print(i)
# part 2: BPJAZGAP
