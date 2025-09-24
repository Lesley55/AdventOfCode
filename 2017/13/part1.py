input = open("input.txt")
input = input.readlines()

layers = []
severity = 0
for i in input:
    layer = i.strip().split(": ")
    l = [int(layer[0]), int(layer[1])]
    
    cycle = l[1] * 2 - 2
    if l[0] % cycle == 0:
        severity += l[0] * l[1]

print(severity)

# part 1: 632
