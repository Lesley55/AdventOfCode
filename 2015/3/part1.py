input = open("input.txt")
input = input.read()

houses = set()
x = 0
y = 0
houses.add(str(x) + "," + str(y))

for i in input:
    if i == "^":
        y += 1
    elif i == "v":
        y -= 1
    elif i == ">":
        x += 1
    elif i == "<":
        x -= 1
    houses.add(str(x) + "," + str(y)) # waarom kan ik hier geen [x,y] adden?

print(len(houses))
