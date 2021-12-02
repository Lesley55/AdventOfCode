import copy

# input by hand, string for chip, int for rtg
floors = [
    [],
    ["3"],
    [3, 4, "4", 5, "5"],
    [1, "1", 2, "2"]
]

# test
floors = [
    [],
    [2],
    [1],
    ["1", "2"]
]

# count chips and rtg's
count = 0
for i in floors:
    count += len(i)

# check if chip gets destroyed by non pair items on floor
def fried(floor, chip):
    rtg = False
    for i in floor:
        if i == chip:
            return False
        elif not type(i) == str:
            rtg = True
    if rtg:
        return True
    return False

# check if no chips get radiated on floor
def safe(floor):
    # remove chips that are together with rtg 
    nonpair = copy.copy(floor)
    for i in floor:
        if type(i) == str:
            if int(i) in nonpair:
                nonpair.remove(i)
    # for whats left without chips that can form a pair check if a chip gets destroyed
    for i in nonpair:
        if type(i) == str:
            if fried(nonpair, int(i)):
                return False
    return True


found = False
next = [[floors, 3, 0]]
previous = []
def check(f, elevator, steps):
    # stop when all chips are at the top/fourth floor
    global found
    if found != False or f in previous:
        return
    if len(f[0]) == count:
        print(f, steps)
        found = steps
        return
    previous.append(f) # dont repeat a configuration already tried
    print(f, steps)
    # move elevator
    elevatorsteps = [-1, 1]
    for k in elevatorsteps:
        for i in f[elevator]:
            # moving a single item with elevator
            if 0 <= elevator + k and elevator + k < len(f):
                    currentfloor = copy.copy(f[elevator])
                    currentfloor.remove(i)
                    nextfloor = copy.copy(f[elevator + k])
                    nextfloor.append(i)
                    if safe(currentfloor) and safe(nextfloor):
                        fl = copy.copy(f)
                        fl[elevator] = currentfloor
                        fl[elevator + k] = nextfloor
                        next.append([fl, elevator + k, steps + 1])
            # moving two items with elevator
            for j in f[elevator]:
                if 0 <= elevator + k and elevator + k < len(f) and i != j:
                    currentfloor = copy.copy(f[elevator])
                    currentfloor.remove(i)
                    currentfloor.remove(j)
                    nextfloor = copy.copy(f[elevator + k])
                    nextfloor.append(i)
                    nextfloor.append(j)
                    if safe(currentfloor) and safe(nextfloor):
                        fl = copy.copy(f)
                        fl[elevator] = currentfloor
                        fl[elevator + k] = nextfloor
                        next.append([fl, elevator + k, steps + 1])

for i in next:
    check(i[0], i[1], i[2])

print(found)

# part 1: 
