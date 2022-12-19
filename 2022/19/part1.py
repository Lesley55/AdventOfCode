import copy
input = open("input.txt")

def collect(time, robots, costs, ores):
    print(time, robots, costs, ores)
    # if out of time, return geodes
    if time <= 0:
        return ores[3]
    # TODO: change to be able to produce different robots in the same minute
    new = []
    for c in range(len(costs)):
        amount = []
        for o in range(len(costs[c])):
            if costs[c][o] > 0:
                if ores[o] > 0 and ores[o] > costs[c][o]:
                    amount.append(int(ores[o] / costs[c][o]))
                else:
                    amount.append(0)
        if min(amount) > 0:
            new.append([c, min(amount)])
    # robots mine ores
    ores = copy.copy(ores)
    for r in range(len(robots)):
        ores[r] += robots[r]
    # get most geodes from possibilities
    geodes = [0]
    if len(new) < 4: # only to allow getting more expensive robot instead of cheapest, not producing if all are possible, doesn't improve yield
        geodes.append(collect(time - 1, robots, costs, ores))
    # produce new robots
    for i in new:
        robots = copy.copy(robots)
        robots[i[0]] += i[1]
        ores = copy.copy(ores)
        for o in range(len(costs[i[0]])):
            ores[o] -= costs[i[0]][o] * i[1]
        geodes.append(collect(time - 1, robots, costs, ores))
    return max(geodes)

quality = 0
for i in input:
    i = i.strip()
    i = i.replace(":", "").split()
    blueprint = int(i[1])
    costs = [[int(i[6]),0,0], [int(i[12]),0,0], [int(i[18]),int(i[21]),0], [int(i[27]),0,int(i[30])]]
    geodes = collect(24, [1,0,0,0], costs, [0,0,0,0])
    quality += blueprint * geodes
    break

print(quality)
# part 1: 
