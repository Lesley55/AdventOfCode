input = open("input.txt")
input = input.read()

houses = set()
x = 0
y = 0
x2 = 0
y2 = 0
houses.add(str(x) + "," + str(y))

for i in range(len(input)):
    if i % 2:
        if input[i] == "^":
            y += 1
        elif input[i] == "v":
            y -= 1
        elif input[i] == ">":
            x += 1
        elif input[i] == "<":
            x -= 1
        houses.add(str(x) + "," + str(y))
    else:
        if input[i] == "^":
            y2 += 1
        elif input[i] == "v":
            y2 -= 1
        elif input[i] == ">":
            x2 += 1
        elif input[i] == "<":
            x2 -= 1
        houses.add(str(x2) + "," + str(y2))


print(len(houses))
