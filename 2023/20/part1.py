input = open("input.txt")

broadcaster = []
modules = {}

for i in input:
    i = i.replace("\n", "").split(" -> ")
    if i[0] == "broadcaster":
        broadcaster = i[1].split(", ")
    else:
        if i[0][0] == "&":
            modules[i[0][1:]] = [i[0][0], False, i[1].split(", "), {}]
        else:
            modules[i[0][1:]] = [i[0][0], False, i[1].split(", ")]

for i in modules:
    for j in modules:
        if i != j and modules[i][0] == "&" and i in modules[j][2]:
            modules[i][3][j] = False

low = 0
high = 0
pressed = 0
while pressed < 1000:
    pressed += 1
    low += len(broadcaster) + 1
    signals = [[b, False] for b in broadcaster]
    while 0 < len(signals):
        new = []
        for signal in signals:
            if not signal[0] in modules:
                continue
            module = modules[signal[0]]
            if module[0] == "%":
                if not signal[1]:
                    modules[signal[0]] = [module[0], not module[1], module[2]]
                    for m in module[2]:
                        new.append([m, not module[1], signal[0]])
                        if not module[1]:
                            high += 1
                        else:
                            low += 1
            elif module[0] == "&":
                recent = module[3]
                recent[signal[2]] = signal[1]
                modules[signal[0]] = [module[0], module[1], module[2], recent]
                all_high = True
                for r in recent:
                    if not recent[r]:
                        all_high = False
                        break
                for m in module[2]:
                    new.append([m, not all_high, signal[0]])
                    if not all_high:
                        high += 1
                    else:
                        low += 1
        signals = new

print(low * high)

# part 1: 929810733
