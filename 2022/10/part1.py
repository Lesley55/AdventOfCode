input = open("input.txt")

x = 1
cycle = 0
v = {}
target = 20
signalsum = 0

def check():
    global x, cycle, v, target, signalsum
    if cycle == target:
        signalsum += cycle * x
        target += 40
    if cycle in v:
        x += v.pop(cycle)

for i in input:
    i = i.strip().split()
    if i[0] == "addx":
        if cycle + 2 in v:
            v[cycle + 2] += int(i[1])
        else:
            v[cycle + 2] = int(i[1])
            check()
            cycle += 1
    check()
    cycle += 1

print(signalsum)
# part 1: 15140
