import copy

input = open("input.txt")

workflows = {}
for i in input:
    if i != "\n" and i[0] != "{":
        i = i.replace("{", " ").replace("}", "").replace("\n", "").split()
        workflows[i[0]] = i[1].split(",")

parts = [["in", {"x": [1, 4000], "m": [1, 4000], "a": [1, 4000], "s": [1, 4000]}]]
new = []
total = 0
while 0 < len(parts):
    for part in parts:
        if part[0] == "R":
            continue
        elif part[0] == "A":
            r = 1
            for i in part[1]:
                r *= 1 + part[1][i][1] - part[1][i][0]
            total += r
            continue
        for rule in workflows[part[0]]:
            if not ":" in rule:
                new.append([rule, part[1]])
                break
            rule = rule.split(":")
            n = int(rule[0][2:])
            c = copy.copy(part[1])
            d = copy.copy(part[1])
            if rule[0][1] == "<":
                if part[1][rule[0][0]][0] < n and n <= part[1][rule[0][0]][1]:
                    c[rule[0][0]] = [c[rule[0][0]][0], n - 1]
                    new.append([rule[1], c])
                    d[rule[0][0]] = [n, d[rule[0][0]][1]]
                    new.append([part[0], d])
                    break
            elif rule[0][1] == ">":
                if part[1][rule[0][0]][0] <= n and n < part[1][rule[0][0]][1]:
                    c[rule[0][0]] = [c[rule[0][0]][0], n]
                    new.append([part[0], c])
                    d[rule[0][0]] = [n + 1, d[rule[0][0]][1]]
                    new.append([rule[1], d])
                    break
    parts = new
    new = []

print(total)

# part 2: 124693661917133
