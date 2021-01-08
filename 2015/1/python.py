input = open("input.txt")
input = input.read()

floor = 0

for x in input:
    if x == "(":
        floor += 1 # beetje jammer dat je bij python niet gwn floor++ kan doen
    else:
        floor -= 1

print(floor)