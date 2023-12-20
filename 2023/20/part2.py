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

pressed = 0
found = False
while not found:
    pressed += 1
    signals = [[b, False] for b in broadcaster]
    while 0 < len(signals):
        new = []
        for signal in signals:
            if not signal[0] in modules:
                if signal[0] == "rx" and not signal[1]:
                    print(pressed)
                    found = True
                    new = []
                    break
                else:
                    continue
            module = modules[signal[0]]
            if module[0] == "%":
                if not signal[1]:
                    modules[signal[0]] = [module[0], not module[1], module[2]]
                    for m in module[2]:
                        new.append([m, not module[1], signal[0]])
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
        signals = new

# part 2: 
