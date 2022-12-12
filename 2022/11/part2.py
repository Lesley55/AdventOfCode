input = open("input.txt")

monkeys = []
for i in input:
    i = i.strip().split(" ")
    if len(i) < 2: continue
    elif i[0] == "Starting":
        monkeys.append({"inspected": 0})
        monkeys[-1]["items"] = []
        for j in i[2:]:
            monkeys[-1]["items"].append(int(j.replace(",", "")))
    elif i[0] == "Operation:":
        monkeys[-1]["op"] = i[3:]
    elif i[0] == "Test:":
        monkeys[-1]["test"] = int(i[3])
    elif i[1] == "true:":
        monkeys[-1]["t"] = int(i[5])
    elif i[1] == "false:":
        monkeys[-1]["f"] = int(i[5])

number = 1
for i in monkeys:
    number *= i["test"]

rounds = 10000
for i in range(rounds):
    for monkey in monkeys:
        for j in range(len(monkey["items"])):
            item = monkey["items"].pop(0)
            # inspect
            a = 0
            b = 0
            if monkey["op"][0] == "old":
                a = item
            else:
                a = int(monkey["op"][0])
            if monkey["op"][2] == "old":
                b = item
            else:
                b = int(monkey["op"][2])
            if monkey["op"][1] == "+":
                item = a + b
            elif monkey["op"][1] == "*":
                item = a * b
                item = item % number
            monkey["inspected"] += 1
            # test and throw
            if item % monkey["test"] == 0:
                monkeys[monkey["t"]]["items"].append(item)
            else:
                monkeys[monkey["f"]]["items"].append(item)

inspected = []
for i in monkeys:
    inspected.append(i["inspected"])
inspected.sort()

print(inspected[-1] * inspected[-2])
# part 2: 13119526120
