import string

input = open("input.txt")

items = ""
group = []
for i in input:
    i = i.strip()
    group.append(i)
    if len(group) == 3:
        for l in group[0]:
            if l in group[1] and l in group[2]:
                items += l
                group = []
                break

alphabet = string.ascii_lowercase + string.ascii_uppercase
sum = 0
for i in items:
    sum += alphabet.index(i) + 1

print(sum)
# part 2: 2631
