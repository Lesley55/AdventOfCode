input = open("input.txt")

ingredients = []

for i in input:
    j = i.replace(",", "").split()
    ingredients.append([int(j[2]), int(j[4]), int(j[6]), int(j[8]), int(j[10])])

highest = 0

# i think this can be optimized better
for i in range(101):
    for j in range(101-i):
        for k in range(101-i-j):
            for l in range(101-i-j-k):
                if i+j+k+l == 100:
                    capacity = 0
                    durability = 0
                    flavor = 0
                    texture = 0
                    letters = [i, j, k, l]
                    for m in range(len(ingredients)):
                        capacity += letters[m] * ingredients[m][0]
                        durability += letters[m] * ingredients[m][1]
                        flavor += letters[m] * ingredients[m][2]
                        texture += letters[m] * ingredients[m][3]
                    if capacity < 0:
                        capacity = 0
                    if durability < 0:
                        durability = 0
                    if flavor < 0:
                        flavor = 0
                    if texture < 0:
                        texture = 0
                    total = capacity * durability * flavor * texture
                    if total > highest:
                        highest = total

print(highest)

# part 1: 18965440