input = "1321131112"

# for x in range(40): # part 1
for x in range(50): # part 2
    new = ""
    p = ""
    c = 1
    for i in input:
        if p == "":
            p = i
        elif i == p:
            c += 1
        else:
            new += str(c) + p
            p = i
            c = 1
    new += str(c) + p
    input = new

print(len(input))

# part 1: 492982
# part 1: 6989950
