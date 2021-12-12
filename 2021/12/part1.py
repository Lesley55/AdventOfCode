import copy

input = open("input.txt")

conn = []
for i in input:
    i = i.strip().split("-")
    conn.append(i)

possible = 0
def next(traveled, step):
    global possible
    t = copy.copy(traveled)
    t.append(step)
    if step == "end":
        possible += 1
        return
    for i in range(len(conn)):
        if step == conn[i][0]:
            if conn[i][1].islower():
                if conn[i][1] in t:
                    continue
            next(t, conn[i][1])
        elif step == conn[i][1]:
            if conn[i][0].islower():
                if conn[i][0] in t:
                    continue
            next(t, conn[i][0])

next([], "start")
print(possible)

# part 1: 4691
