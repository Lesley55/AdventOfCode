input = open("input.txt")

df = []

for i in input:
    j = i.strip().split()
    k = j[0].split("-")
    df.append([int(j[1][:-1]), int(j[2][:-1]), int(j[3][:-1]), int(j[4][:-1])])

viable = 0

for i in range(len(df)):
    for j in range(len(df)):
        if i != j and df[i][1] > 0 and df[i][1] <= df[j][2]:
            viable += 1

print(viable)

# part 1: 981
