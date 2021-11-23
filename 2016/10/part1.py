input = open("input.txt")


def giveToNext(name, number, value):
    if name == "bot":
        bots[number].give(value)
    elif name == "output":
        if number in outputs:
            outputs[number].append(value)
        else:
            outputs[number] = [value]


class Bot():
    def __init__(self, id, l, low, h, high):
        self.id = id
        self.l = l
        self.low = low
        self.h = h
        self.high = high
        self.microchips = []

    def give(self, chip):
        if len(self.microchips) < 2:
            self.microchips.append(chip)
        else:
            print("oeps")

    def check(self):
        if len(self.microchips) == 2:
            mi = min(self.microchips)
            ma = max(self.microchips)

            if mi == 17 and ma == 61:
                print(self.id)

            self.microchips = []

            giveToNext(self.l, self.low, mi)
            giveToNext(self.h, self.high, ma)


bots = {}
outputs = {}
g = []

# make bots
for i in input:
    i = i.split()
    if i[0] == "bot":
        bots[int(i[1])] = Bot(int(i[1]), i[5], int(i[6]), i[10], int(i[11]))
    else:
        g.append(i)

# give start values to bots
for i in g:
    bots[int(i[5])].give(int(i[1]))

for i in range(100):
    for i in bots:
        bots[i].check()

# part 1: 86
