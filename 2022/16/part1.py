import copy

input = open("input.txt")

valves = {}
for i in input:
    i = i.strip().replace("=", " ").replace(";", "").replace(",", "").split()
    valves[i[1]] = (int(i[5]), i[10:])

most = 0
def next(current, time, open, released, visited):
    global most
    if released > most:
        most = released
        print(open, released)
    if time == 0:
        return
    open, released, visited = copy.copy(open), copy.copy(released), copy.copy(visited)
    for i in valves[current][1]:
        if not current + i in visited:
            next(i, time - 1, open, released, visited + [current + i])
    if valves[current][0] != 0 and current not in open:
        released += (time - 1) * valves[current][0]
        open.append(current)
        next(current, time - 1, open, released, visited)

next("AA", 30, [], 0, [])
print(most)
# part 1: 
