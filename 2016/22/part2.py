input = open("input.txt")

df = {}

for i in input:
    j = i.strip().split()
    k = j[0].split("-")
    # df -> (x, y) = [Size, Used, Avail, Use%]
    df[(int(k[1][1:]), int(k[2][1:]))] = [int(j[1][:-1]), int(j[2][:-1]), int(j[3][:-1]), int(j[4][:-1])]

steps = 0



print(steps)

# part 2: 
