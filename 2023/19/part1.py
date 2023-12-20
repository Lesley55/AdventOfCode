input = open("input.txt")

workflows = {}
parts = []
for i in input:
    if i[0] == "{":
        i = i.replace("{", "").replace("}", "").replace("\n", "").replace("=", ",").split(",")
        part = {}
        for j in range(0, len(i), 2):
            part[i[j]] = int(i[j+1])
        parts.append(part)
    elif i != "\n":
        i = i.replace("{", " ").replace("}", "").replace("\n", "").split()
        workflows[i[0]] = i[1].split(",")

total = 0
for part in parts:
    flow = "in"
    stop = False
    while not stop:
        for rule in workflows[flow]:
            if not ":" in rule:
                flow = rule
                break
            rule = rule.split(":")
            if rule[0][1] == "<":
                if part[rule[0][0]] < int(rule[0][2:]):
                    flow = rule[1]
                    break
            elif rule[0][1] == ">":
                if part[rule[0][0]] > int(rule[0][2:]):
                    flow = rule[1]
                    break
        if flow == "R":
            stop = True
        elif flow == "A":
            for xmas in part:
                total += part[xmas]
            stop = True

print(total)

# part 1: 346230
