input = open("input.txt")
input = input.read()

floor = 0
index = 0
first = True

for x in input:
    if floor == -1:
        first = False
    if x == "(":
        floor += 1 # beetje jammer dat je bij python niet gwn floor++ kan doen
    else:
        floor -= 1
    if first:
        index += 1

print(floor)
print(index)