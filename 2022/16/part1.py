input = open("input.txt")

valves = {}
for i in input:
    i = i.strip().replace("=", " ").replace(";", "").replace(",", "").split()
    valves[i[1]] = (int(i[5]), i[10:])

dist = {}
def get_path_lengths(start, current, steps, visited):
    if not current in visited:
        if steps > 0 and valves[current][0] > 0:
            dist[start].append([current, steps])
        for i in valves[current][1]:
            get_path_lengths(start, i, steps + 1, visited + [current])

for i in valves:
    dist[i] = []
    get_path_lengths(i, i, 0, [])

most = 0
def next(current, time, open, released):
    global most
    if released > most:
        most = released
        print(released, open)
    if time <= 0:
        return
    for i in dist[current]:
        if i[0] != current:
            next(i[0], time - i[1], open, released)
    if not current in open:
        next(current, time - 1, open + [current], released + (time - 1) * valves[current][0])

next("AA", 30, [], 0)
print(most)
# part 1: 
