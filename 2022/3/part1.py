import string

input = open("input.txt")

items = ""
for i in input:
    i = i.strip()
    a, b = i[:len(i)//2], i[len(i)//2:]
    for l in a:
        if l in b:
            items += l
            break

alphabet = string.ascii_lowercase + string.ascii_uppercase
sum = 0
for i in items:
    sum += alphabet.index(i) + 1

print(sum)
# part 1: 8243
