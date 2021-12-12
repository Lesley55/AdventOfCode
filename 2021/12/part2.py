import copy

input = open("input.txt")

conn = []
for i in input:
    i = i.strip().split("-")
    conn.append(i)

possible = 0
def next(traveled, step, small):
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
                    if small and conn[i][1] != "start":
                        next(t, conn[i][1], False)
                    continue
            next(t, conn[i][1], small)
        elif step == conn[i][1]:
            if conn[i][0].islower():
                if conn[i][0] in t:
                    if small and conn[i][0] != "start":
                        next(t, conn[i][0], False)
                    continue
            next(t, conn[i][0], small)

next([], "start", True)
print(possible)

# part 2: 140718
